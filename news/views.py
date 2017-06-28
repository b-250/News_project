# encoding: utf-8

from django.shortcuts import render
from news.models import Mynews
from django.views.decorators.csrf import csrf_exempt
from newsbackend.common import respond_assemble

import getnews

def showindex(request):
    return render(request, 'index.html')

@csrf_exempt
def change2json(news_list):
    news_json_list = []
    for news in news_list:
        news_json = {}
        news_json['title'] = news.title
        news_json['id'] = news.id
        news_json['src'] = news.src
        news_json['weburl'] = news.weburl
        news_json['time'] = news.time
        news_json['pic'] = news.pic
        #print(news_json)
        news_json_list.append(news_json)
    return  news_json_list

@csrf_exempt
def get_news(request):
    channel = request.POST.get('channel')
    num = int(request.POST.get('num'))
    begin = int(request.POST.get('begin'))
    print(channel)
    if channel == 'rec':
        if request.user.is_authenticated():
            last = Mynews.objects.last()
            news_list = Mynews.objects.filter(id__gt = last.id-10)
        else:
            news_channel = Mynews.objects.filter(channel='hot')
            order_news = news_channel.order_by('-id')
            news_list = order_news.all()[0:num]
    else :
        news_channel = Mynews.objects.filter(channel=channel)
        order_news = news_channel.order_by('-id')
        end = begin + num
        news_list = order_news.all()[begin:end]
        #last = news_channel.last()

        #news_list = news_channel.filter(id__gt=last.id-10)
    body = change2json(news_list)
    print(news_list)
    return respond_assemble(code=1,msg='news',body=body)


@csrf_exempt
def news_update(request):
    num = 30
    news_list = getnews.mynews.update_news(num)
    for new in news_list:
        channel = new['category']
        src = new['src']
        mobileurl = new['url']
        title = new['title']
        weburl = new['weburl']
        pic = new['pic']
        time = new['time']
        savepath = new['savepath']
        #print(savepath)
        print(title)
        #print(channel)
        #print(new)
        news = Mynews.objects.filter(title=title)
        if news.exists():
            continue
        else:
            mylist = Mynews.objects.create(channel=channel,src=src,mobileurl=mobileurl,title=title,weburl=weburl,pic=pic,time=time,savepath=savepath)

    return respond_assemble(code=1, msg='')

if __name__=="__main__":
    news_update()