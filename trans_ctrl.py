# coding=utf-8
import urllib.request    
from HandleJs import Py4Js
from clipboard import gettext
from pynput import mouse,keyboard
import re
    
def open_url(url):    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}      
    req = urllib.request.Request(url = url,headers=headers)  
    response = urllib.request.urlopen(req)
    data = response.read()
    data = data.decode('utf-8')
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

old = ''

def on_press(key):
    
    #print(key);
    
    #import pdb
    #pdb.set_trace()

    if key is keyboard.Key.esc:

        #pastes = gettext().decode('UTF-8', 'ignore')
        pastes = gettext().decode('GBK')
        pastes = pastes.strip().strip(b'\x00'.decode())
        pastes = pastes.replace('\r\n',' ')
        pastes = pastes.lower()
        pastes = pastes.replace('e.g.','such as ')
        pastes = pastes.replace('etc.','such as ')
        pastes = pastes.replace('et al.','')
        pastes = pastes.replace('<','less than ')
    
        global old
        if pastes != old:
  
            old = pastes[:]

            #sentences = pastes.split('.')
            sentences = re.split('[.?!;] ', pastes)

            for content in sentences:
            
                js = Py4Js()
                tk = js.getTk(content)    
                translate(content,tk)  
                print(content)
                print()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
