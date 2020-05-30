import urllib.request, urllib.parse, urllib.error
import re
import socket
import urllib.parse

def downloadWeb(url,pageId):
    if url in urlMap:
        pass
    else:
        pageId += 1
        urlMap[url]=pageId
        idMap[pageId]=url
        htmlFile=open('./output/'+(str(pageId)+'.txt'),'wb')
        htmlFile.write(urllib.request.urlopen(url).read())
        htmlFile.close()
        
        htmlFile=open('./output/'+(str(pageId)+'.txt'),'r')
        for line in htmlFile:
            ans=re.findall(pattern,line)
            for one in ans :
                urlTail=one.split('"')[1]            
                url=urllib.parse.urljoin(url,urlTail)
                if url in urlMap:
                    print('skip---'+url)
                else:
                    print('download---'+url)
                    pageId += 1
                    urlMap[url]=pageId
                    idMap[pageId]=url
                    catchFile=open('./output/'+(str(urlMap[url])+'.txt'),'wb')
                    try:
                        catchFile.write(urllib.request.urlopen(url).read())
                    except:
                        pass
                    finally:
                        catchFile.close()               
        htmlFile.close()

    urlMapFile=open('./output/map.txt','w')
    for key in list(idMap.keys()):
        urlMapFile.write(str(key)+'\t'+str(idMap[key])+'\n')
    urlMapFile.close()
    
    print('success!')


if __name__=='__main__':
    socket.setdefaulttimeout(10)

    entrance='http://www.zju.edu.cn/'
    pattern=re.compile('href="[^(javascript)]\S*[^(#)(css)(js)(ico)]\"')
    pageId=0
    idMap={}
    urlMap={}
    downloadWeb(entrance,pageId)