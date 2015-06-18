import time
import sys
import urllib
import getopt
import re
import os
opts,args=getopt.getopt(sys.argv[1:],"d:u:o:")
time_interval=""
url=""
path=""
print(opts)
for op,value in opts:
    if op=="-d":
        time_interval=value
    elif op=="-u":
        url=value
    else:
        path=value
isExists=os.path.exists(path)
if not isExists:
    print('make dir!')
    os.makedirs(path)
while(True):
    cur_time=time.strftime("%Y%m%d%H%M") #current time
    cur_path=path+'\\'+cur_time
    os.makedirs(cur_path+'\\images'),os.mkdir(cur_path+'\\css'),os.mkdir(cur_path+'\\js')
    content=urllib.urlopen(url).read()
    open(cur_path+'\\index.html','w').write(content)
    reg_list=[r'src="(.*?(\.jpg))"',r'href="(.*?(\.css))"',r'src="(.*?(\.js))"']
    for i in range(len(reg_list)):
        reg_com=re.compile(reg_list[i])
        content_list=re.findall(reg_com,content)
        x=1
        if i==0:
            final_path=cur_path+'\\images\\'
        elif i==1:
            final_path=cur_path+'\\css\\'
        else:
            final_path=cur_path+'\\js\\'
        for j in content_list:
            urllib.urlretrieve(j[0],final_path+str(x)+j[1])
            x=x+1
    print('done!')
    time.sleep(float(time_interval))



