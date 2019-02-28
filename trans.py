# coding=utf-8
import urllib.request    
from HandleJs import Py4Js
from clipboard import gettext
import time
import re
    
def open_url(url):    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}      
    req = urllib.request.Request(url = url,headers=headers)  
    response = urllib.request.urlopen(req)    
    data = response.read().decode('utf-8')    
    return data    
    
def translate(content,tk):    
    if len(content) > 4891:    
        print("Input too long")    
        return     
        
    content = urllib.parse.quote(content)    
        
    url = "http://translate.google.cn/translate_a/single?client=t"+ "&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca"+"&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1"+"&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s"%(tk,content)    
          
    result = open_url(url)    
        
    end = result.find("\",")    
    if end > 4:    
        print(result[4:end])

   
def main():  

    old = ''

    while 1:

        time.sleep(1)

        pastes = gettext().decode('UTF-8', 'ignore').strip().strip(b'\x00'.decode())
        pastes = pastes.replace('\r\n',' ')
    
        if pastes != old:
  
            old = pastes[:]

            #sentences = pastes.split('.')

            #import pdb
            #pdb.set_trace() 

            sentences = re.split('[.?!;]', pastes)


 
            for content in sentences:
            
                if content == 'q!':    
                    break    
            
                js = Py4Js()
                tk = js.getTk(content)    
                translate(content,tk)  
                print(content)
                print()
    
        
if __name__ == "__main__":    
    main()  