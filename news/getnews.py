# encoding: utf-8

import json
from urllib import urlencode
import requests
import os
import time
# 解决编码问题
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

class newsapi:
    AppKey = '2f6318c5608bca1f'

    @staticmethod
    def get_channel(timeout=1):
        """
        获取新闻频道 https://api.jisuapi.com/news/channel
        :param timeout: request时长限制
        :return: 渠道list
        """
        url = 'https://api.jisuapi.com/news/channel?'
        params = {'appkey': newsapi.AppKey}
        params_encoded = urlencode(params)
        try:
            response = requests.get(url, params=params_encoded, timeout=timeout).json()
            if response['status'] == '0':
                return response['result']
        except:
            pass
        return None

    @staticmethod
    def get_news(channel, num, timeout=1):
        """
        从单一频道获取新闻 https://api.jisuapi.com/news/get
        :param channel: 频道
        :param timeout: request时长限制
        :return: 新闻list
        """
        url = 'http://api.jisuapi.com/news/get?'
        params = {'appkey': newsapi.AppKey, 'start': 0, 'num': num, 'channel': channel}
        params_encoded = urlencode(params)
        try:
            response = requests.get(url, params=params_encoded, timeout=timeout).json()
            # print(response)
            if response['status'] == '0':
                return response['result']['list']
        except:
            pass
        return None

    @staticmethod
    def search_news(keyword, timeout=1):
        """
        搜索新闻 https://api.jisuapi.com/news/search
        :param keyword: 搜索关键词
        :param timeout: request时长限制
        :return: 新闻list
        """
        url = 'https://api.jisuapi.com/news/search'
        params = {'appkey': newsapi.AppKey, 'keyword': keyword}
        params_encoded = urlencode(params)
        try:
            response = requests.get(url, params=params_encoded, timeout=timeout).json()
            if response['status'] == '0':
                return response['result']['list']
        except:
            pass
        return None

class mynews:
    @staticmethod
    def store_list(content,channel):
        """
        存储最新新闻的文件列表
        :param content: 最新新闻文件列表
        :param channel: channel,如果是总表则输入空串
        :return: null
        """
        filename = 'news/news/'+ channel + '/newfilelist.json'
        with open(filename,'w') as json_file:
            json.dump(content,json_file)

    @staticmethod
    def store_json(news_content,channel):
        """
        存储新闻内容为json
        :param news_content: 新闻内容
        :param channel: channel
        :return: 返回文件名
        """
        path = 'news/news/'+channel+'/'
        if not os.path.isdir(path):
            os.mkdir(path)
        filename = path + news_content['title'] + '.json'
        with open(filename,'w') as json_file:
            json.dump(news_content,json_file)
        json_file.close()
        return filename

    @staticmethod
    def load_json(filename):
        """
        载入新闻的json文件
        :param filename: 需要载入的文件名
        :return: 文件内容
        """
        with open(filename) as json_file:
            contents = json.load(json_file)
        return contents

    @staticmethod
    def load_news(new_file_list):
        """
        载入指定列表的新闻
        :param new_file_list: 需要载入的列表
        :return: null
        """
        for new_file in new_file_list:
            print(new_file)
            news = mynews.load_json(new_file)
            print(news['title'])

    @staticmethod
    def update_news(num):
        """
        更新新闻
        :return: 新闻json文件名总表
        """
        '''
        channel_list = newsapi.get_channel(1)
        while(channel_list == None):
            print('retry to get the channel')
            time.sleep(10)
            channel_list = newsapi.get_channel(1)
        '''
        channel_list = ['头条']#, '新闻', '财经', '体育', '娱乐', '军事', '教育', '科技', 'NBA', '股票']
        print(channel_list)
        new_file_list = []
        #num = 10
        for channel in channel_list:
            print(channel)
            news_list = newsapi.get_news(channel, num, 2)
            cnt = 0
            while news_list == None:
                cnt += 1
                print('retry to get the news of '+channel)
                time.sleep(10)
                news_list = newsapi.get_news(channel, num, 2)
                if cnt > 10:
                    print('have try 10 times!')
                    break

            #print(news_list)
            channel_new_file_list =[]
            for i in range(0, num):
                #print(i)
                print(news_list[i])
                filename = mynews.store_json(news_list[i], channel)
                channel_new_file_list.append(filename)
                news_list[i]['savepath'] = filename
                new_file_list.append(news_list[i])
            mynews.store_list(channel_new_file_list,channel)
        return new_file_list

if __name__=="__main__":
    new_file_list = mynews.update_news(10)
    #new_file_list = ['news/头条/易到:乐视挪用易到资金系诽谤.json', 'news/头条/曝齐祖铁定留任！哪怕没冠军.json', 'news/头条/被称中国台北队 台湾有人急了.json', 'news/头条/富力斯帅:对榜首不感兴趣.json', 'news/头条/游泳冠军赛刘湘50自折桂.json', 'news/头条/冠军赛孙杨1500自夺冠.json', 'news/头条/今年年底将发射嫦娥五号.json', 'news/头条/外国记者滞留朝鲜机场.json', 'news/头条/国民党回应台代表队称呼被改.json', 'news/头条/中国机群南海曾与外军机缠.json', 'news/新闻/山东检察对徐玉玉案提起公诉.json', 'news/新闻/项俊波被免去领导职务.json', 'news/新闻/郑州版“光明区信访局”整改.json', 'news/新闻/国民党回应台代表队称呼被改.json', 'news/新闻/济南查处阻碍环保部督查组案.json', 'news/新闻/中方回应美韩部署萨德立场.json', 'news/新闻/贵阳客车坠河已致13死6伤.json', 'news/新闻/特朗普政府将对日施压.json', 'news/新闻/埃尔多安或不会提前议会选举.json', 'news/新闻/韩媒:萨德完成部署4月来不及 .json']
    print(new_file_list)
    mynews.store_list(new_file_list,'')
    #mynews.load_news(new_file_list)