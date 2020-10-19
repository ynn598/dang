from django.shortcuts import redirect, render
from django.utils.deprecation import MiddlewareMixin

from user.models import TUser


class MyMiddleware(MiddlewareMixin):  # 自定义的中间件
    def __init__(self, get_response):  # 初始化
        super().__init__(get_response)
        print("初始化")

    # view处理请求前执行
    def process_request(self, request):  # 某一个view
        return 0


    # 在process_request之后 View之前执行
    def process_view(self, request, view_func, view_args, view_kwargs):
        if "index" in request.path or 'booklist' in request.path or 'book_detail' in request.path or 'cart' in request.path:
            user_name = request.COOKIES.get("user_name")
            password = request.COOKIES.get("password")
            is_login = request.session.get("is_login")
            print("cookie.............", user_name, password)
            request.session['user_name'] = user_name
            result = TUser.objects.filter(user_name=user_name, password=password)
            if is_login:
                print(22222222222222)
                pass
            else:
                if result:
                    request.session['is_login']=True
                    return redirect("index:index")
        if "indent" in request.path or "indent_ok" in request.path:
            print("强制登录")
            url = request.GET.get("url")
            request.session['url']=url
            is_login = request.session.get("user_name")
            if is_login:
                pass
            else:
                return render(request,"login.html",{"url":url})


    # view执行之后，响应之前执行
    def process_response(self, request, response):
        print("response:", request, response)
        return response  # 必须返回response

    # 如果View中抛出了异常
    def process_exception(self, request, ex):  # View中出现异常时执行
        print("exception:", request, ex)