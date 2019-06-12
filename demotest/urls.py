from django.conf.urls import url
from .import views
app_name='demotest'
urlpatterns=(

    # url('',views.hello,name='hello'),
     #url('topics/',views.topics,name='topics'),
    #url('^topics/(?P<topic_id>\d+)/$',views.topic,name='topic')
    #r让Django将这个字符串视为原始字符串，并指出正则表达式包含在括号内
    #这个表达式的(?P<topic_id>\d+)与包含在两个斜杠的整数匹配，并将这个整数储存在一个名为topic_id的实参中
    #这部分两边的表达式括号捕获url中的值；
    #?P<topic_id>将匹配得到值存储到topic_id中；
    #而表达式\d+与包含在两个斜杠内的任何数字都匹配，不管这个数字为多少
     url(r'^add/$',views.add,name='add'),
     url(r'^deletes/$',views.deletes,name='deletes'),
     url(r'^updates/$',views.updates,name='updates'),
     url(r'^checks/$',views.checks,name='check'),

)