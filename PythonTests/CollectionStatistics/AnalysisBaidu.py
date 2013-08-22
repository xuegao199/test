#coding=gbk
from bs4 import BeautifulSoup
import codecs
import re,time
from lxml import etree
import urllib,urllib2,gevent
import _mysql
import MySQLdb as mdb
import sys
import math
'''
 统计google,baidu,360,yahoo,qqsoso,sougou 对365auto.com的收录情况
'''


GOOGLE_URL='http://www.google.com.hk/search?q=site%3A365auto.com'
GOOGLE_URL_TW='http://www.google.com/search?q=site%3A365auto.com'
BAIDU_URL='http://www.baidu.com/s?wd=site%3A365auto.com'
S360_URL='http://www.so.com/s?ie=utf-8&src=360sou_home&q=site%3A365auto.com'
YAHOO_URL='http://search.yahoo.com/search;_ylt=A0oGdUg.9z9R5A0AZdJXNyoA?p=site%3A365auto.com'
SOSO_QQ_URL='http://www.soso.com/q?w=site%3A365auto.com'
SOUGOU_URL='http://www.sogou.com/web?query=site%3A365auto.com'

'''
    get Google Collection count of 365auto.com
'''
def getGoogleCollectionStatistics():
    return 0
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.160 Safari/537.22'),
                         ('scheme','https'),
                         ('version','HTTP/1.1'),
                         ('cookie','PREF=ID=80b5177d2f559838:U=7997c93143bf8a12:FF=2:LD=zh-CN:TM=1353994513:LM=1362982528:GM=1:S=H6dZ6l4zFxgoiAo-; SID=DQAAAMAAAABG2fN2Bqe0Jxi-lHXHGZdLqAoXaDFeYy0EZBi04nRDI6ZADXrDbLjvwS5yH6CYAHMTaXkQHIEeJqX4l-308C-lhlFXsamVHfUhA7hMm7RVY6TcpjA_qjg3CKowSCsgDDQMZnYkXDwGpOo-Fp0qYE9HOIYS_rrNCRLpg-zsQ72JGhf5CZpTd4muga-Rb6p_OlnKWkIHeolU53AXfCbHAamojoUXb_THKW91XzA9s5mnrbZObgAUsvY2c6HTsAFROL0; HSID=Awg2ulK5-dUwnVqfk; SSID=AIWgis7ztF_OfhjTJ; APISID=G1pv0MF-uH6VSapT/A1bCuE952ReRqdoYj; SAPISID=CaoU04gInMv9HaQU/A-fQWGvKYm4ZjOliy; NID=67=i3a5tVYTZvL5KRaKnH939G4lijS_xE5LNhI7OtAhcVls05mCrmzWPjMi6hWoWDCq7EEvxDFUMnBaeoFxpgEwYjoG_Q9wsSmuxdYCFRyr6Luz4DaiOgKjEwvIe5Jg8G41DL96-56SF97XfQVYjUmeC5NH4VX_xm_vgpCyfaaLzMbBSDP8qj4VJj3cpZ5hW4TgRGg3FvcjaNzNj-sgeszIfx4')]
    gpage = opener.open(GOOGLE_URL).read()
    soup = BeautifulSoup(gpage,from_encoding="UTF-8")
    count = soup.find(id="resultStats")
    print u'GOOGLE:%s'%count
    r = re.compile(u'u\'找到约 (.*) 条结果.*\'')
    for string in count.strings:
        cs = repr(string).decode('unicode_escape')
        s_match = r.findall(cs)
        for c in s_match:
            count = c
    return count

'''
    get Google Collection count of 365auto.com
'''
def getGoogleTWCollectionStatistics():
    return 0
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.160 Safari/537.22'),
                         ('scheme','https'),
                         ('version','HTTP/1.1'),
                         ('cookie','PREF=ID=80b5177d2f559838:U=7997c93143bf8a12:FF=2:LD=zh-CN:TM=1353994513:LM=1362982528:GM=1:S=H6dZ6l4zFxgoiAo-; SID=DQAAAMAAAABG2fN2Bqe0Jxi-lHXHGZdLqAoXaDFeYy0EZBi04nRDI6ZADXrDbLjvwS5yH6CYAHMTaXkQHIEeJqX4l-308C-lhlFXsamVHfUhA7hMm7RVY6TcpjA_qjg3CKowSCsgDDQMZnYkXDwGpOo-Fp0qYE9HOIYS_rrNCRLpg-zsQ72JGhf5CZpTd4muga-Rb6p_OlnKWkIHeolU53AXfCbHAamojoUXb_THKW91XzA9s5mnrbZObgAUsvY2c6HTsAFROL0; HSID=Awg2ulK5-dUwnVqfk; SSID=AIWgis7ztF_OfhjTJ; APISID=G1pv0MF-uH6VSapT/A1bCuE952ReRqdoYj; SAPISID=CaoU04gInMv9HaQU/A-fQWGvKYm4ZjOliy; NID=67=i3a5tVYTZvL5KRaKnH939G4lijS_xE5LNhI7OtAhcVls05mCrmzWPjMi6hWoWDCq7EEvxDFUMnBaeoFxpgEwYjoG_Q9wsSmuxdYCFRyr6Luz4DaiOgKjEwvIe5Jg8G41DL96-56SF97XfQVYjUmeC5NH4VX_xm_vgpCyfaaLzMbBSDP8qj4VJj3cpZ5hW4TgRGg3FvcjaNzNj-sgeszIfx4')]
    gpage = opener.open(GOOGLE_URL_TW).read()
    soup = BeautifulSoup(gpage,from_encoding="UTF-8")
    count = soup.find(id="resultStats")
    print u'GOOGLE:%s'%count
    r = re.compile(u'u\'找到约 (.*) 条结果.*\'')
    for string in count.strings:
        cs = repr(string).decode('unicode_escape')
        s_match = r.findall(cs)
        for c in s_match:
            count = c
    return count

'''
    get baidu Collection count of 365auto.com
'''
def getBaiduCollectionStatistics(pageUrl):
    #print u'Get page data:%s'%pageUrl
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.160 Safari/537.22'),
                         ('scheme','https'),
                         ('version','HTTP/1.1')]
    gpage = opener.open(pageUrl).read()
    soup = BeautifulSoup(gpage,from_encoding="UTF-8")
    #print soup
    urlsArray = soup.find_all("span",class_="g")
    #for ul in urlsArray:
    #    print ul.text
    return urlsArray

'''
'''
def getBaiduCollections():
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.160 Safari/537.22'),
                         ('scheme','https'),
                         ('version','HTTP/1.1')]
    gpage = opener.open(BAIDU_URL).read()
    soup = BeautifulSoup(gpage,from_encoding="UTF-8")
    count = soup.find('p','site_tip').strong
    r = re.compile(u'找到相关结果数(\d*)个。')
    s_match = r.findall(count.string)
    for c in s_match:
        count = c
    print 'Count%s:'%count
    urls = []
    for page in range(0, 280, 10):
        pageUrl ='http://www.baidu.com/s?wd=site%3A365auto.com&pn='+str(page)+'&ie=utf-8'
        print 'Get page:%s'%page
        pageUrls = getBaiduCollectionStatistics(pageUrl)
        for ul in pageUrls:
            #print ul.text
            urls.append(ul)
    print 'Got %s data'%(str(len(urls)))
    r = re.compile('([^/]*)(.*)([^\xa0]*)(\d{4}-\d{1,2}-\d{1,2}).*')
    for ul in urls:
        urlText = ul.text
        #print 'SRC:%s==>'%urlText,
        s_match = r.findall(urlText)
        for m in s_match:
           #print 'M0:%s'%m[0],
           #print 'M1:%s'%m[1],
           #print 'M2:%s==>MS:'%m[3],
           #print int(time.mktime(time.strptime(m[3], "%Y-%m-%d")))*1000
           saveResult(m[0],m[1],m[3])



'''
 sava result to mysql
'''
def saveResult(domain,inurl,srcDate):
    con = None
    try:
        con = mdb.connect('127.0.0.1', 'root','', 'test')
        con.set_character_set('utf8')
        cur = con.cursor()
        cur.execute("INSERT INTO baidu_collect(domain,uri,date,create_time) VALUES('%s','%s','%s',SYSDATE())"%(domain,inurl,srcDate))
    except _mysql.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    finally:
        if con:
            con.commit()
            con.close()

if __name__ == '__main__':
    try:
	    #bc=getBaiduCollectionStatistics()
        getBaiduCollections()
    except:
       1==1

