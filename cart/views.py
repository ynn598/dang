from django.http import JsonResponse
from django.shortcuts import render, redirect

from cart.models import TCart
from index.models import TBook

# 渲染购物车
def cart(request):
    user_name = request.session.get("user_name")
    # 登陆状态下
    if user_name:
        user_id = request.session.get("user_id")
        book_ids = TCart.objects.filter(user_id=user_id)
        sum = 0
        booklists = []
        moneys=[]
        sum_money = 0
        for i in book_ids:
            booklist = TBook.objects.filter(id=i.book_id).values("id","book_name","picture","now_price","tcart__count","price")
            count = TCart.objects.filter(book_id=i.book_id)[0].count
            now_price = TBook.objects.filter(id=i.book_id)[0].now_price
            money = count * now_price
            moneys.append(money)
            sum_money +=money
            print("里面的数量:",count)
            sum += count
            booklists.append(booklist)
        moneys = list(reversed(moneys))
        request.session["sum_count"] = sum
        request.session['sum_money']=sum_money
        content = {"user_name": user_name, "booklists":booklists,"sum":sum,"moneys":moneys,"sum_money":sum_money}

        return render(request, "car.html", content)
    else:
        cart = request.session.get("cart")
        if cart:
            sum = cart.size()
            request.session["sum_count"] = sum
            return render(request,"car.html", {"user_name":user_name,"cart":cart,"sum":sum})
        else:
            request.session["sum_count"] = 0
            return render(request, "car.html", {"user_name": user_name, "cart": cart})

# 往购物车里面加东西
def add_cart(request):
    book_id = request.GET.get("book_id")
    count= int(request.GET.get("count"))
    user_id = request.session.get("user_id")
    user_name = request.session.get("user_name")
    if user_name:
        uu = TCart.objects.filter(user_id=user_id)
        sum = 0
        for i in uu:
            sum+=i.count
        print('sumddddd',sum)
        result = TCart.objects.filter(user_id=user_id,book_id=book_id)
        if result:
            result[0].count+=count
            result[0].save()
        else:
            TCart.objects.create(book_id=book_id,user_id=user_id,count=count)
        return JsonResponse({"t":1,"count":count,"sum":sum})
    else:
        request.session["count1"]=count    #把书的数量存起来
        cart = request.session.get("cart")# 先把书添加到购物车, 再存到session里面, 但是得判断一下,要是用cart里的方法, 就需要构造一个cart方法
        if cart:
            cart.add_book(id=book_id)
        else:
            cart = Cart()
            cart.add_book(id=book_id)
        request.session["cart"] = cart
        sum = cart.size()
        return JsonResponse({"t":1,"count":count,'sum':sum})


# 从购物车里面删除
def delete(request):
    book_id = request.GET.get("book_id")
    user_name = request.session.get("user_name")
    if user_name:
        tcart = TCart.objects.get(book_id=book_id)
        tcart.delete()
        return redirect("cart:cart")
    else:
        cart = request.session.get("cart")
        cart.remove_book(id=book_id)
        request.session["cart"] = cart
        return JsonResponse({"txt": 1})


# 退出时候的操作
def exit(request):
    try:
        del request.session['user_name']   #清楚某一个key的值
        del request.session['is_login']
        res = redirect('user:login')
        user_name = request.COOKIES.get("user_name")
        password = request.COOKIES.get("password")
        res.set_cookie("user_name",user_name,max_age=0)
        res.set_cookie("password",password,max_age=0)
        return res
    except Exception as e:
        print(e)
        return e


class Book:
    def __init__(self, id, count):
        book = TBook.objects.get(pk=id)
        self.id = book.id
        self.name = book.book_name
        self.count = count
        self.price = book.now_price
        self.picture = book.picture
    def money(self):
        return self.count*self.price

class Cart:
    def __init__(self):
        self.book_list = []   #构造购物车这个列表
        self.__index=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < len(self.book_list):
            item=self.book_list[self.__index]
            self.__index += 1
            return item
        else:
            self.__index = 0
            raise StopIteration

    # 首先是查找, 看这本书是否在购物车里面
    def get_book(self, id):
        for book in self.book_list:
            # 如果要添加的这本书在购物车的列表里, 就返回这本书(book对象)
            if int(book.id) == int(id):
                return book

    def money(self):
        sum = 0
        for book in self.book_list:
            sum +=book.count*book.price
        return sum

    # 将一本书添加到购物车列表里,
    # 如果在购物车列表里只需要将列表里该书的数目加一即可
    # 如果购物车里没有这本书, 就把它添加到购物车这个列表里
    def add_book(self, id, count=1):
        book = self.get_book(id)
        if book:
            book.count += count
        else:
            book = Book(id=id, count=count)
            self.book_list.append(book)

    #删除书的操作
    def remove_book(self, id):
        print(id)
        book = self.get_book(id)
        print(self.book_list[0].id)
        self.book_list.remove(book)

    def size(self):
        sum = 0
        for book in self.book_list:
            sum+=book.count
        return sum