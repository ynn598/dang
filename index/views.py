import os,django
from copy import deepcopy
from django.core.paginator import Paginator
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dangdang.settings")
django.setup()

from django.shortcuts import render
from index.models import TCategory, TBook


def index(request):
    cate1 = TCategory.objects.filter(level=1)
    cate2 = TCategory.objects.filter(level=2)
    user_name = request.session.get("user_name")
    # 新书推荐
    booklist = TBook.objects.filter().order_by('public_time')
    # 新书热卖

    sales = TBook.objects.filter(public_time__gte="2020-1-1").order_by("sale")[0:6]
    # 推荐
    money = TBook.objects.filter().order_by("money")
    content = {"cate1": cate1, "cate2": cate2, 'booklist': booklist, "sales": sales, 'money': money,"user_name":user_name}
    return render(request, "index.html", content)


def booklist(request):
    cate1 = TCategory.objects.filter(level=1)
    cate2 = TCategory.objects.filter(level=2)
    # 查询类别,如果点的是一级表
    cate_id = request.GET.get("cate_id")
    print(cate_id)
    level = TCategory.objects.filter(id=cate_id)[0].level
    # 如果是一级列表
    if level==1:
        cates = TCategory.objects.filter(parent_id=cate_id)
        # 创建一个空的queryset对象
        books = TBook.objects.filter(cate_id=0)
        for i in cates:
            tbooks = TBook.objects.filter(cate_id=i.id)
            books = books | tbooks
        big_cate_name = TCategory.objects.filter(id=cate_id)[0].cate_name
        cate_name=""
    else:
        books = TBook.objects.filter(cate_id=cate_id)
        cate_name = TCategory.objects.filter(id=cate_id)[0].cate_name
        big_cate_id = TCategory.objects.filter(id=cate_id)[0].parent_id
        big_cate_name = TCategory.objects.filter(id=big_cate_id)[0].cate_name
    # 分页
    pagtor = Paginator(books, per_page=3)
    count = pagtor.num_pages   #总页数
    num = request.GET.get("num", 1)
    print(num)
    page = pagtor.page(num)
    sum = 0
    for i in books:
        sum += 1
    user_name = request.session.get("user_name")
    content = {"sum": sum, "count": count, "num": num,  "cate1": cate1, "cate2": cate2, "page": page,
               "big_cate_name": big_cate_name, "cate_name": cate_name, "cate_id": cate_id,"user_name":user_name}
    return render(request, 'booklist.html', content)


def book_detail(request):
    book_id = request.GET.get("book_id")
    cate_id = TBook.objects.filter(id=book_id)[0].cate_id  #小类的id
    big_cate_id = TCategory.objects.filter(id=cate_id)[0].parent_id
    big_cate_name = TCategory.objects.filter(id=big_cate_id)[0].cate_name
    cate_name = TCategory.objects.filter(id=cate_id)[0].cate_name
    book = TBook.objects.filter(id=book_id)
    user_name = request.session.get("user_name")
    content = {"book":book,"big_cate_name":big_cate_name,"cate_name":cate_name,"cate_id":cate_id,"big_cate_id":big_cate_id,"user_name":user_name,"book_id":book_id}
    return render(request,"Book details.html",content)
