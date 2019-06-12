from django.conf.urls import url
from .import views
app_name='learning_logs'
# urlpatterns=(
#     url('',views.index,name='index'),
#     url('topics/',views.topics,name='topics'),
   #   url('^topics/(?P<topic_id>\d+)/$',views.topic,name='topic')
#     #r让Django将这个字符串视为原始字符串，并指出正则表达式包含在括号内
#     #这个表达式的(?P<topic_id>\d+)与包含在两个斜杠的整数匹配，并将这个整数储存在一个名为topic_id的实参中
#     #这部分两边的表达式括号捕获url中的值；
#     #?P<topic_id>将匹配得到值存储到topic_id中；
#     #而表达式\d+与包含在两个斜杠内的任何数字都匹配，不管这个数字为多少
#
# )
urlpatterns = [
    # index

    url(r'^$', views.index, name='index'),

    # show all topics
    url(r'^topics/$', views.topics, name='topics'),

    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    url(r'^new_topic/$',views.new_topic,name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),

    url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry'),
    url(r'delete/$',views.deletes,name='deletes')

]

