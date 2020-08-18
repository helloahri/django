from django.urls import path
from book.views import index, test, catid,gett,post,post_json,get_header,response,jsonres,retest
# from book.views import URLParam1View
from book.views import paramview
from book.views import set_cookies,get_cookies,del_cookies,register


from book.views import set_session,get_session

urlpatterns = [
    path('index/', index),
    path('test/', test),
    # path('<cat_id>/<id>/', catid),
    path('gett/',gett),
    path('post/',post),
    path('postjson/',post_json),
    path('param/<int:age>/',paramview.as_view()),
    path('getheader/',get_header),
    path('response/',response),
    path('jsonres/',jsonres),
    path('redirect/',retest),
    path('setcookie/',set_cookies),
    path('getcookie/',get_cookies),
    path('delcookie/',del_cookies),
    path('setsession/',set_session),
    path('getsession/',get_session),
    path('register/',register.as_view())




    # path('param/<int:age>/',URLParam1View.as_view())

]


