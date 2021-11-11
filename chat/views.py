from django.conf.urls import url
from django.shortcuts import redirect, render
from datetime import date
from datetime import datetime
import os
import qrcode
import socket

hostname=socket.gethostname()
ipaddr=socket.gethostbyname(hostname)

st="http://"+ipaddr+":8000"

img=qrcode.make(st)
addr=os.getcwd()
print(addr)
img.save(addr+"/chat/static/chat/images/"+"scan.jpg")


today=date.today().strftime('%d %b %y')
time=datetime.now().strftime('%H : %M')

msg=[]

# Create your views here.
def home(request):

    try:

        name=request.GET['name']

        return redirect("/"+name)

    except:

        return render(request,'chat/home.html',{'URL':st})


def det(request,name):

    try:
                
        today=date.today().strftime('%d %b %y')
        time=datetime.now().strftime('%H : %M')

        s=request.GET['message']

        msg.append([name,s,time,today])

        return render(request,'chat/details.html',{'message_sent':msg,'name':name})

    except:
        return render(request,'chat/details.html',{'message_sent':msg,'name':name})

