# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
import hashlib #md5E
from django.template.context_processors import request
import time, datetime
from date_part import date_part
from dateutil.parser import parse
from md5jiemi import md5jiemi

def hello(request):
    return render(request, "index.html")

    
def http_get(request):
    path = "输入接口地址，形如：http://1.1.1.1:8080/xxx"
    message = ""
    if request.POST:
        path = request.POST['qpath']
        if path:
            try:
                header  =  {
                        'Content-Type': 'application/json'
                }   
                path =  request.POST['qpath'] #py2
                url = "" + path #api url
                r = requests.get(url, headers=header)
                message = r.text
            except Exception:
                 message = '检查填写是否正确~'

    return render(request, 'web_api_get.html',{ 
                                                'path':path,
                                                'message':message,
                                                            })

def http_post(request):
    path = "输入接口地址，形如：http://1.1.1.1:8080/xxx"
    message = "当前只支持application/json形式"
    body = "输入body"
    if request.POST:
        path = request.POST['qpath']
        body = request.POST['qbody']
        if path:
            try:
                header  =  {
                        'Content-Type': 'application/json'
                }   
                path =  request.POST['qpath'] #py2
                body = request.POST['qbody']
                url = "" + path #api url
                r = requests.post(url, data=body,headers=header)
                message = r.text
            except Exception:
                 message = '检查填写是否正确~'

    return render(request, 'web_api_post.html',{ 
                                                'path':path,
                                                'message':message,
                                                'body':body,
                                                            })

def py_json(request):
    
    if request.POST:
        form_commit = request.POST['q']
        if form_commit:
            try:
                js = json.loads(form_commit)
                json.dumps(js)
                message = json.dumps(js,indent=3,ensure_ascii=False)
                #下边这个方法也可以
                # loads=demjson.decode(form_commit)
                # message=json.dumps(loads, indent=3, sort_keys=False, ensure_ascii=False)
            except Exception:
                 message = '您提交的json格式不正确哦~'

        else: 
            form_commit = u'''    {
                                "Json解析":"输入你的json吧！"
                                
                                }'''
            message = u'请输入你的json代码吧~'

    else:
        form_commit = u'''      {
                                "Json解析":"输入你的json吧！"
                                
                                }'''
        message = u'左侧框内输入json哦~'

    #return render(request, 'tools/pyjson.html',ctx)
    return render(request, 'pyjson.html',{'message':message, 
                                                'form_commit':form_commit,
                                                            })
    
    
def md5Encrypt(request):
    '''py2 use following. start md5jiami
    '''
    import sys #要重新载入sys。因为 Python 初始化后会删除 sys.setdefaultencoding 这个方 法
    reload(sys) 
    sys.setdefaultencoding('utf-8')
    data = "1234"
    str_final = ""
    data2 = "81dc9bdb52d04dc20036dbd8313ed055"
    str_final2 = ""
    if request.POST.has_key('md5jiami'):
        if request.POST:
            data = request.POST['qdata']
    #         str_final = request.POST['str_final']
            if data:
                try:
                    m = hashlib.md5()
                    data = request.POST['qdata']
                    #待加密的字符串
                    str_original = request.POST['qdata']
                    #生成加密串
                    str_middle = m.update(str_original)
                    #获取加密串
                    str_final = m.hexdigest() 
                    '''py2 use following. start
                    '''
                except Exception:
                     str_final = '检查填写是否正确~'
                    
                #     '''py3 use following. start
                #     '''
                #     import hashlib
                #     data = 'abcd去'
                #     str_final =hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
                #     print (str_final)
                #     '''py3 use following. end
                #     '''
    '''floowing is py2  md5jiemi
    '''
    if request.POST.has_key('md5jiemi'):
        if request.POST:
            data2 = request.POST['qdata2']
    #         str_final = request.POST['str_final']
            if data2:
                try:
                    text = data2
                    str_final2 = md5jiemi(text)
                except Exception:
                     str_final2 = '用户过多，稍后重试~'
 
    return render(request, 'md5Encrypt.html',{'str_final':str_final, 
                                              'data':data,
                                              'str_final2':str_final2, 
                                              'data2':data2,
                                                            })
    
def date_differ(request):
    date_commit1 = u'2018-01-01'  #tianshujisuan
    date_commit2 = u'2030-01-01' #tianshujisuan
    differ_result =u'' #tianshujisuan
    message = u'' #tianshujisuan
    date1 = '2018-08-01 02:03:04' #
    rslt_timeStamp_s = ''
    rslt_timeStamp2date =u''
    timestamp1 = u'1533060184'
    rslt_timeStamp_ms = u''
    
    diff_days = ''
    diff_week = ''
    diff_month = ''
    diff_year = ''
    diff_s = ''
    diff_detail = ''
    date_time1 = '2018-10-01 12:12:12'
    date_time2 = '2020-9-01 12:12:10'
    
    
    if request.POST:#tianshujisuan
        if request.POST.has_key('date_differ'):
            date_commit1 = request.POST['q']
            date_commit2 = request.POST['q2']
            if date_commit1 or date_commit2:
                try:
                    date_commit1 = date_commit1
                    date_commit2 = date_commit2
                    d1 = date_part(date=date_commit1)
                    d2 = date_part(date=date_commit2)
                    differ_result = (d2-d1).days
                    message = u''
                except Exception:
                    differ_result =u''
                    message = '您提交的格式不正确哦~'
    
        if request.POST.has_key('date2timeStamp'):  #date2timeStamp
            date1 = request.POST['qdate1']
            if date1:
                try:
                    date1 = date1
                    timeArray = time.strptime(date1, "%Y-%m-%d %H:%M:%S")
                    rslt_timeStamp_s = int(time.mktime(timeArray))
                    print(rslt_timeStamp_s)
                    rslt_timeStamp_ms = str(rslt_timeStamp_s) + "000"
                    print(rslt_timeStamp_ms)
                except Exception:
                    rslt_timeStamp_s =u''
                    rslt_timeStamp_ms =u''

        if request.POST.has_key('timeStamp2date'):  #timeStamp2date
            timestamp1 = request.POST['qtimestamp1']
            if timestamp1:
                try:
                    timestamp = timestamp1
                    timestamp = int(timestamp[0:10])
                    #转换成localtime
                    time_local = time.localtime(timestamp)
                    #转换成新的时间格式(2016-05-05 20:28:54)
                    rslt_timeStamp2date = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
                except Exception:
                    rslt_timeStamp2date =u''
                    
        
        if request.POST.has_key('time_differ'):  #timeStamp2date
            date_time1 = request.POST['qdate_time1']
            date_time2 = request.POST['qdate_time2']

            if date_time1 or date_time2:
                try:
                    b = parse(date_time1)
                    a = parse(date_time2)
                    diff_days = (a-b).days
                    print (diff_days)
                    diff_week = int(diff_days/7)
                    print (diff_week)
                    diff_s = (a-b).total_seconds()
                    diff_s = int(diff_s)
                    print (diff_s)
                    diff_month = diff_days / 4 / 7
                    diff_year = int (diff_days / 365)
                    # print ((a-b).seconds) #仅计算时分秒的时间差
                    
                    diff_detail = str(datetime.timedelta(seconds=diff_s))
                    print(diff_detail)
                except Exception:
                    diff_days = ''
                    diff_week = ''
                    diff_s = ''
                    diff_detail = ''
                    date_time1 = ''
                    date_time2 = ''
                    diff_month = ''
                    diff_year = ''
                    

    return render(request, 'time_date.html',{
                                                'date_commit1':date_commit1, 
                                                'date_commit2':date_commit2,
                                                'differ_result':differ_result,
                                                'message':message,
                                                'date1':date1, 
                                                'rslt_timeStamp_s':rslt_timeStamp_s,
                                                'rslt_timeStamp2date':rslt_timeStamp2date,
                                                'timestamp1':timestamp1,
                                                'rslt_timeStamp_ms':rslt_timeStamp_ms,
                                                'diff_days':diff_days,
                                                'diff_week':diff_week,
                                                'diff_s':diff_s,
                                                'diff_detail':diff_detail,
                                                'date_time1':date_time1,
                                                'date_time2':date_time2,
                                                'diff_month':diff_month,
                                                'diff_year':diff_year,
                                                
                                                                                                     })

def deal_string(request):
    import sys #要重新载入sys。因为 Python 初始化后会删除 sys.setdefaultencoding 这个方 法
    reload(sys)
    sys.setdefaultencoding('utf-8')

    result = ''

    if request.POST:
        #压缩
        if request.POST.has_key('str_compress'):
            form_commit = request.POST['q']
            if form_commit:
                try:
                    result = form_commit.strip().replace(' ', '').replace('\n', '').replace('\t', '').replace('\r', '').strip()

                except Exception:
                     result = u'检查输入是否正确'
        #转义
        if request.POST.has_key('str_transfer'):
            form_commit = request.POST['q']
            if form_commit:
                try:
                    result = form_commit.replace('"', '\\"')

                except Exception:
                     result = u'检查输入是否正确'
        #去除转义
        if request.POST.has_key('str_untransfer'):
            form_commit = request.POST['q']
            if form_commit:
                try:
                    result = form_commit.replace('\\"', '"')

                except Exception:
                     result = u'检查输入是否正确'
        #中文转unicode
        if request.POST.has_key('str_china2unicode'):
            form_commit = request.POST['q']
            if form_commit:
                try:
                    result = json.dumps(form_commit)
                    result = result[1:-1]

                except Exception:
                     result = u'检查输入是否正确'
        #unicode转中文
        if request.POST.has_key('str_unicode2china'):
            form_commit = request.POST['q']
            if form_commit:
                try:
                    result = form_commit.decode('unicode_escape')
                    #result = result[1:-1]

                except Exception:
                     result = u'检查输入是否正确'

    return render(request, 'deal_string.html',{
                                                'result':result,
                                                            })
