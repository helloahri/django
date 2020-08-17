from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View

from book.models import BookInfo,PeopleInfo
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.

import json

def jsonres(request):

    return JsonResponse({'city':'beijing','age':'18'})


def retest(request):

    return redirect('/index')



def response(request):

    response =  HttpResponse(content="itcast python",content_type='text/html',status=400)
    response['itcast'] = 'aaaaaa'

    return response

    # response = HttpResponse(content='itcast python')
    # response.status_code = 400
    # response['itcast'] = 'ppyytthhoonn'




def index(request):
    return HttpResponse("index_OK")

def catid(request,cat_id,id):
    return JsonResponse({'cat_id':cat_id,'id':id})


def gett(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a)  # 3
    print(b)  # 2
    print(alist)  # ['1', '3']
    return HttpResponse('OK')

def post(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('OK')

def post_json(request):
    req_data = json.loads(request.body)
    print(request.body)
    print(req_data['a'])
    print(req_data['b'])
    return HttpResponse("post_json___OK")

class paramview(View):

    def get(self, request, age):

        return HttpResponse(f"path的age是：{age}")

        # return HttpResponse('测试path()提取普通路径参数：%s' % age)


def get_header(request):
    print(request.META['CONTENT_TYPE'])
    contenttype = request.META['CONTENT_TYPE']
    return HttpResponse(contenttype)






# class URLParam1View(View):
#     """测试path()提取普通路径参数
#     http://127.0.0.1:8000/url_param1/18/
#     """
#
#     def get(self, request, age):
#         """
#         :param age: 路由提取的关键字参数
#         """
#         return HttpResponse('测试path()提取普通路径参数：%s' % age)




def test(request):
    # books = BookInfo.objects.all()

    # for book in books:
    #     print(book.name)

    # bbb = BookInfo.objects.all()[0:1]
    # print(bbb)

    from django.core.paginator import Paginator

    booooks = BookInfo.objects.all()
    fenye = Paginator(booooks,2)

    # print(fenye)
    print(fenye.page(1))
    print(fenye.num_pages)


    return HttpResponse("TEST   OK")

