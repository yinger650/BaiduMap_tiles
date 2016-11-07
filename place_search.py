# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 13:27:28 2016

@author: Min
"""
import urllib
import urllib2
import json
import codecs

akey = 'uzIatbtHgfCTr71dWxnHolfZqG6vARNc'

def request_place_API(lat1,lng1,lat2,lng2,query,page):
    bounds = lat1+","+lng1+","+lat2+","+lng2
    url='http://api.map.baidu.com/place/v2/search'
    args = {'query':query,
            'page_size':10,
            'page_num':page,
            'bounds':bounds,
            'output':'json',
            'ak':akey}
    data = urllib.urlencode(args)
    #req = urllib2.Request(url, data)
    response = urllib2.urlopen(url+'?'+data)
    result = response.read()
    #print result
    return result
        
def request_place_API_all(lat1,lng1,lat2,lng2,query):
    pre_result = request_place_API(lat1,lng1,lat2,lng2,query,0)
    a = json.loads(pre_result)
    tot = a["total"]
    result_list =  a["results"]
    for i in range(1,tot//10+1):
        i_result = request_place_API(lat1,lng1,lat2,lng2,query,i)
        b = json.loads(i_result)
        result_list += b["results"]
    return result_list
    
def store_results(result,filename):
    f = codecs.open(filename,'w','utf-8')
    for block in result:
        f.write(block[u'name']+"\n")
        lat = block[u'location'][u'lat']
        lng = block[u'location'][u'lng']
        f.write(str(lat)+' '+str(lng)+'\n')
        #f.write(unicode(block[u'location'],'utf-8'))
    f.close()
    
def clean_list(a):
    b = set()
    result = []
    for block in a:
        name = block[u'name']
        if name not in b:
            b.add(name)
            result.append(block)
    return result
        

if __name__ == "__main__":
    lat1 = '31.022547'
    lng1 = '121.429391'
    lat2 = '31.041453'
    lng2 = '121.45749'
    #query = "楼"
    blocks_in_SJTU = [];
    blocks_in_SJTU += request_place_API_all(lat1,lng1,lat2,lng2,"楼")
    blocks_in_SJTU += request_place_API_all(lat1,lng1,lat2,lng2,"中心")
    blocks_in_SJTU += request_place_API_all(lat1,lng1,lat2,lng2,"馆")
    blocks_in_SJTU += request_place_API_all(lat1,lng1,lat2,lng2,"宿舍")
    blocks_in_SJTU += request_place_API_all(lat1,lng1,lat2,lng2,"学生公寓")
    blocks_in_SJTU += request_place_API_all(lat1,lng1,lat2,lng2,"院")
    blocks_in_SJTU = clean_list(blocks_in_SJTU)
    filename = "result.txt"
    store_results(blocks_in_SJTU, filename)
    
    
    
    