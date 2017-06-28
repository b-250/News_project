# encoding: utf-8

from django.shortcuts import render
from news.models import Mynews
from django.views.decorators.csrf import csrf_exempt
from newsbackend.common import respond_assemble
from users.models import UserSetting
import getnews

c_list = ['finance','sports','ent','mil','edu','tech','nba','stock']

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
        print(news_json)
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

def get_rec(likelist,num,base):
    ch_list = dict(finance=0,sports=0,ent=0,mil=0,edu=0,tech=0,nba=0,stock=0,sum=0)
    sum = 0.0
    ch_list['finance'] = likelist.finance
    sum += likelist.finance
    ch_list['sports'] = likelist.sports
    sum += likelist.sports
    ch_list['ent'] = likelist.ent
    sum += likelist.ent
    ch_list['mil'] = likelist.mil
    sum += likelist.mil
    ch_list['edu'] = likelist.edu
    sum += likelist.edu
    ch_list['tech'] = likelist.tech
    sum += likelist.tech
    ch_list['nba'] = likelist.nba
    sum += likelist.nba
    ch_list['stock'] = likelist.stock
    sum += likelist.stock
    news_list = []
    allnewslist = Mynews.objects.order_by('-id')
    for ch in c_list:
        print(ch_list[ch])
        ch_list[ch] /=sum
        ch_list[ch] *= 10
        print(ch_list[ch])
        avg = int(round(ch_list[ch]))
        print(avg)
        news = allnewslist.filter(channel=ch)
        if avg > 1:
            for i in range(avg):
                news_list.append(news.all()[base*avg+i])
        elif avg == 1:
            print(news.all()[i].title)
            news_list.append(news.all()[base])

        #print(news_list)
    return news_list

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
            likelist = UserSetting.objects.get(userid=user.id)
            news_list = get_rec(likelist,num,begin/10)

            # last = Mynews.objects.last()
            # news_list = Mynews.objects.filter(id__gt = last.id-10)
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
    newsid = int(request.GET.get('newsid'))
    newscontent = Mynews.objects.get(id = newsid)
    channel = newscontent.channel
    if request.user.is_authenticated():
        user = request.user
        likelist = UserSetting.objects.get(userid=user.id)
        update_setting(channel,likelist,5)

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