from django.shortcuts import render
from learning_logs.models import Topic,Entry
from django.http import HttpResponseRedirect
from learning_logs.forms import TopicForm,EntryForm

# Create your views here.
def index(request):
    return render(request,'learning_logs/index.html')
def topics(request):
    topics=Topic.objects.order_by('date_added')
    context={'topics':topics}
    return render(request,'learning_logs/topics.html',context)
def topic(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by('-date_added')#减号指的是降序
    context={'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)
'''
利用(?P<topic_id>d+)捕获的值，传入topic()视图中并获取他，
再将获取到进行降序排序，即显示最近的主题和条目并保存到context的字典中
最后再传回topic.html文件中
'''
def new_topic(request):
    #未提交数据：创建一个新表单
    if request.method!='POST':
        form=TopicForm()
    else:
        form=TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reversed('learning_logs:topics.html'))
    context={'form':form}
    print("i am oklkld")
    return render(request,'learning_logs/new_topic.html',context)
def new_entry(request,topic_id):
    '''在待定的主题中添加新条目'''
    topic=Topic.objects.get(id=topic_id)
    if request.method!='POST':
        print("i am okla")
       #这里创建的新表单form有问题，导致加入的entry内容进不去，数据库也不行
        form=EntryForm()
    else:
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            #这里的跳转跳不过去
            return HttpResponseRedirect(reversed('learning_logs:topic',args=[topic_id]))
        context={'topic':topic,'form':form}
        return render(request,'learning_logs/new_entry.html',context)
def edit_entry(request,entry_id):
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic
    if request.method!='POST':
        form=EntryForm(instance=entry)#创建一根EntryForm表单实例，并使用instance是他可以把当前的文本填充
    else:                              #用户将可以看到并编辑
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reversed('learning_logs:topics',args=[topic.id]))
            #return render(request,'learning_logs/topic.html')
    context={'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)
def deletes(request):
    sql_topic=Topic.objects.get(id=12)
    sql_topic.delete()
    return render(request,'learning_logs/index.html')
    #return HttpResponseRedirect(reversed('learning_logs:index'))