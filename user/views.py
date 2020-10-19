from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from cart.models import TCart
from index.models import TBook
from user.models import TUser
from captcha.image import ImageCaptcha
import random, string

# 注册页面的渲染
def register(request):
    return render(request,"register.html")

# 登录界面的渲染
def login(request):
    # 这里存在一个记住密码, 进入登录页面之前需要判断一下session中是否记录的有用户名
    url = request.GET.get("url")
    book_id = request.GET.get("book_id")
    cate_id = request.GET.get("cate_id")
    if book_id:
        url = url+'?book_id='+book_id
    if cate_id:
        url = url+'?cate_id='+cate_id
    request.session["url"]=url

    user_name = request.COOKIES.get("user_name")
    password = request.COOKIES.get("password")
    print("cookie.............", user_name, password)
    request.session['user_name']=user_name
    result = TUser.objects.filter(user_name=user_name,password=password)
    if result:
        return redirect("index:index")
    else:
        return render(request,"login.html")

# 用户名字的验证
def user_name_logic(request):
    user_name = request.GET.get("user_name")
    result = TUser.objects.filter(user_name=user_name)
    if result:
        content="no"   #已存在
    else:
        content="ok"
    return HttpResponse(content)

# 生成验证码
def get_captcha(request):
    code_list = random.sample(string.ascii_lowercase+string.ascii_uppercase+string.digits,4)
    random_code = "".join(code_list)
    print(random_code)
    request.session["code"]=random_code
    data = ImageCaptcha().generate(random_code)  #生成图片
    return HttpResponse(data,"static/image/png")

# 核对验证码
def check_code(request):
    captcha = request.GET.get("captcha")
    code = request.session.get("code")
    print(captcha,code)
    if str(captcha).lower()==str(code).lower():
        return JsonResponse({"content":1})
    else:
        return JsonResponse({"content":0})

# 注册逻辑
def register_logic(request):
    user_name = request.GET.get("txt_username")
    password = request.GET.get("txt_password")
    request.session["user_name"]=user_name
    TUser.objects.create(user_name=user_name,password=password)
    request.session["is_login"] = True
    return JsonResponse({"content":"ok"})

# 注册成功页面的渲染
def register_ok(request):
    user_name = request.session.get("user_name")
    user_id = TUser.objects.filter(user_name=user_name)[0].id
    request.session["user_id"]=user_id
    url = request.session.get("url")
    return render(request,"register ok.html",{"user_name":user_name,"url":url})

# 登录逻辑
def login_logic(request):
    user_name = request.GET.get("user_name")
    password = request.GET.get("password")
    remember = request.GET.get("remember")
    print(remember,"remember",user_name)
    result = TUser.objects.filter(user_name=user_name,password=password)
    user_id = TUser.objects.get(user_name=user_name).id
    request.session["user_id"] = user_id
    if result:
        url = request.session.get("url")
        if url:
            res = JsonResponse({"text": 1, "user_name": user_name,"url":url,"flag":1})
        else:
            res = JsonResponse({"text": 1, "user_name": user_name, "flag":0})
        # 如果点击了记住密码, 实现下面这个函数
        if int(remember)==1:
            res.set_cookie("user_name",user_name,max_age=7*24*60*60)
            res.set_cookie("password",password,max_age=7*24*60*60)
        user_id = TUser.objects.get(user_name=user_name).id

        cart = request.session.get("cart")
        if cart:
            for book in cart:
                tbook = TCart.objects.filter(book_id=book.id)
                print("tbok",tbook)
                if tbook:
                    print("took.count",tbook.count)
                    tbook[0].count = int(tbook[0].count) + int(book.count)
                    print(222,tbook[0].count)
                    tbook[0].save()
                else:
                    TCart.objects.create(book_id=book.id,user_id=user_id,count=book.count)
            del request.session['cart']
        request.session["is_login"]=True
        request.session["user_id"]=user_id
        request.session["user_name"]=user_name  #将成功登陆的用户名存在session中
        return res  #成功登陆
    else:
        return JsonResponse({"text":0})

# 注册成功后点击立即购物返回的界面
def shopping(request):
    url = request.session.get("url")
    if url:
        return JsonResponse({"url":url,"flag":1})
    else:
        return JsonResponse({"flag":0})