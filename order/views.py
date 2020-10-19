import random
import string
import time

from django.http import JsonResponse
from django.shortcuts import render
from cart.models import TCart
from index.models import TBook

from order.models import TAddress, TOrderItem, TOrder
from user.models import TUser


def indent(request):# 收货地址页面的渲染
    user_name= request.session.get("user_name")
    user_id = request.session.get("user_id")
    booklist = TCart.objects.filter(user_id=user_id)
    print(user_id,222222222222222222222222222222222222222)
    auto_address = TAddress.objects.filter(user_id=user_id)
    books=[]
    discounts = []
    little_money = []
    sum = 0
    for book in booklist:
        tbook = TBook.objects.filter(id=book.book_id).values("id", "book_name", "press", "now_price","price","tcart__count")
        print(tbook)
        books.append(tbook)
        count = TCart.objects.filter(book_id=book.book_id)[0].count
        now_price = TBook.objects.filter(id=book.book_id)[0].now_price
        price = TBook.objects.filter(id=book.book_id)[0].price
        discount = now_price/price*10
        discount="%.2f"%discount
        discounts.append(discount)
        money=count*now_price
        little_money.append(money)
    for i in little_money:
        sum += i
    request.session["sum"]=sum
    discounts = list(reversed(discounts))
    little_money=list(reversed(little_money))
    content = {"user_name":user_name,"books":books,'discounts':discounts,"little_money":little_money,'sum':sum,"auto_address":auto_address}
    return render(request,"indent.html",content)

# 订单成功页面的渲染
def indent_ok(request):
    user_name = request.session.get("user_name")
    order = request.session.get("order")
    sum_count = request.session.get("sum_count")
    order_id = request.session.get("order_id")
    print(sum_count)
    sum_money = request.session.get("sum_money")
    return render(request,"indent ok.html",{"user_name":user_name,"order":order,"sum_count":sum_count,"order_id":order_id,"sum_money":sum_money})

# 收货地址逻辑   点击提交订单时的操作
def address_logic(request):
    person = request.GET.get("person")
    address = request.GET.get("address")
    post_code = request.GET.get("post_code")
    telephone = request.GET.get("telephone")
    cellphone = request.GET.get("cellphone")
    user_name = request.session.get("user_name")
    new_time = time.strftime("%Y-%m-%d",time.localtime())
    user_id = TUser.objects.filter(user_name=user_name)[0].id
    # 生成收货地址
    result = TAddress.objects.filter(user_id=user_id, address=address, post_code=post_code, cellphone=cellphone,telephone=telephone, person=person)
    if result:
        print("改地址已存在")
        pass
    else:
        TAddress.objects.create(user_id=user_id, address=address, post_code=post_code, cellphone=cellphone,telephone=telephone, person=person)
    address_id = TAddress.objects.filter(user_id=user_id, address=address, post_code=post_code, cellphone=cellphone,telephone=telephone, person=person)[0].id
    # 生成订单号
    code_list = random.sample(string.digits, 10)
    order_id = "".join(code_list)
    request.session['order_id']=order_id
    # 生成订单
    sum = request.session.get("sum")
    order = TOrder.objects.create(receive=person,send="当当自营店",new_time=new_time,sum_price=sum,order_id=order_id,address_id=address_id,user_id=user_id)
    request.session["order"]=order
    id_order = TOrder.objects.filter(receive=person,send="当当自营店",new_time=new_time,sum_price=sum,order_id=order_id,address_id=address_id,user_id=user_id)[0].id

    # 生成订单项表
    tcart = TCart.objects.filter(user_id=user_id)
    for book in tcart:
        count = book.count
        book_id = book.book_id
        print("count",count,book_id)
        TOrderItem.objects.create(count=count,book_id=book_id,order_id=id_order)
    tcart.delete()
    return JsonResponse({"text":1})

def auto_address(request):
    address_id = request.GET.get("address_id")
    print(address_id)
    address = TAddress.objects.get(id=address_id)
    print(address)
    def mydefault(e):
        return {"person":e.person,"address":e.address,"post_code":e.post_code,"cellphone":e.cellphone,"telephone":e.telephone}

    print(address.person)
    return JsonResponse(address, safe=False,json_dumps_params={"default":mydefault})
