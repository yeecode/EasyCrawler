import urllib
import re
import socket
import urlparse

def downloadWeb(url,pageId):
    if urlMap.has_key(url):
        pass
    else:
        pageId += 1
        urlMap[url]=pageId
        idMap[pageId]=url
        htmlFile=open('./output/'+(str(pageId)+'.txt'),'w')
        htmlFile.write(urllib.urlopen(url).read())
        htmlFile.close()
        
        htmlFile=open('./output/'+(str(pageId)+'.txt'),'r')
        for line in htmlFile:
            ans=re.findall(pattern,line)
            for one in ans :
                urlTail=one.split('"')[1]            
                url=urlparse.urljoin(url,urlTail)
                if urlMap.has_key(url):
                    print 'skip---'+url
                else:
                    print 'download---'+url
                    pageId += 1
                    urlMap[url]=pageId
                    idMap[pageId]=url
                    catchFile=open('./output/'+(str(urlMap[url])+'.txt'),'w')
                    try:
                        catchFile.write(urllib.urlopen(url).read())
                    except:
                        pass
                    finally:
                        catchFile.close()               
        htmlFile.close()

    urlMapFile=open('./output/map.txt','w')
    for key in idMap.keys():
        urlMapFile.write(str(key)+'\t'+str(idMap[key])+'\n')
    urlMapFile.close()
    
    print 'success!'


if __name__=='__main__':
    socket.setdefaulttimeout(10)

    entrance='http://www.zju.edu.cn/'
    pattern=re.compile('href="[^(javascript)]\S*[^(#)(css)(js)(ico)]\"')
    pageId=0
    idMap={}
    urlMap={}
    downloadWeb(entrance,pageId)