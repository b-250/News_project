# encoding: utf-8

from django.shortcuts import render
from news.models import Mynews
from django.views.decorators.csrf import csrf_exempt
from newsbackend.common import respond_assemble
from users.models import UserSetting
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

def update_setting(channel, likelist, num):
    if channel == 'finance':
        likelist.finance = likelist.finance+num
        likelist.save()
    elif channel == 'sports':
        likelist.sports = likelist.sports+num
        likelist.save()
    elif channel == 'ent':
        likelist.ent = likelist.ent+num
        likelist.save()
    elif channel == 'mil':
        likelist.mil = likelist.mil+num
        likelist.save()
    elif channel == 'edu':
        likelist.edu = likelist.edu+num
        likelist.save()
    elif channel == 'tech':
        likelist.tech = likelist.tech+num
        likelist.save()
    elif channel == 'nba':
        likelist.nba = likelist.nba+num
        likelist.save()
    elif channel == 'stock':
        likelist.stock = likelist.stock+num
        likelist.save()

@csrf_exempt
def get_news(request):
    channel = request.POST.get('channel')
    num = int(request.POST.get('num'))
    begin = int(request.POST.get('begin'))
    print(channel)
    if request.user.is_authenticated():
        user = request.user
        likelist = UserSetting.objects.get(userid=user.id)
        update_setting(channel,likelist,2)

    if channel == 'rec':
        if request.user.is_authenticated():
            last = Mynews.objects.last()
            news_list = Mynews.objects.filter(id__gt = last.id-10)
        else:
            news_channel = Mynews.objects.filter(channel='hot')
            order_news = news_channel.order_by('-id')
            news_list = order_news.all()[0:num]
    else:
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

@csrf_exempt
def news_content(request):
    #newsid = int(request.GET.get('newsid'))
    #print(newsid)
    return render(request,'newscontent.html')

@csrf_exempt
def get_content(request):
    newsid = int(request.GET.get('newsid'))
    print(newsid)
    newscontent = Mynews.objects.get(id = newsid)
    savepath = newscontent.savepath
    cotent = getnews.mynews.load_json(savepath)
    print(cotent)
    body = dict(title=newscontent.title,time=newscontent.time,weburl=newscontent.weburl,content=cotent,channel=newscontent.channel,src=newscontent.src)
    return respond_assemble(code=1,body=body)
    #return respond_assemble(code=0)

if __name__=="__main__":
    news_update()