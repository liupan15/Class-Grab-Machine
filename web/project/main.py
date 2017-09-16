from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth import login
from model.models import *

def home(request):
    return HttpResponse('index.html');

def sign2(request):
    return render(request, 'sign_in.html'); 

def sign1(request):
    return render(request, 'sign_up.html');

def sign_up(request):
    #print("haipa");
    if request.POST:
        Userid = request.POST['ID'];
        #content['User'] = Userid;
        Password = request.POST['Password'];
        if(not User.objects.filter(username = Userid)):
            data = User(username = Userid, password = Password);
            data.save();
            dataplus = UserPlus(userid = Userid, user = data);
            dataplus.save();
            login(request, data);
            #print(request.user.is_authenticated());
            #print("haipa");
        else:
            return HttpResponseRedirect('/2/');
    return HttpResponseRedirect('/main/');

def sign_in(request):
    if request.POST:
        Userid = request.POST['ID'];
        Password = request.POST['Password'];
        data = User.objects.get(username = Userid);
        login(request, data);
        return HttpResponseRedirect('/main/');
    #return HttpResponseRedirect('/2/');

def main(request):
    flag = False;
    content = {};
    if request.user.is_authenticated():  #是否已经登陆
        #flag = 1;
        content['User'] = request.user.username;
        print(request.user);
#    if request.POST:
#        Userid = request.POST['ID'];
#        content['User'] = Userid;
#        Password = request.POST['Password'];
#        if(not User.objects.filter(username = Userid)):
#            data = User(username = Userid, password = Password);
#            data.save();
#            dataplus = UserPlus(userid = Userid, user = data);
#            dataplus.save();
    if request.GET:
        
        if request.GET['id1']:
            Userid = request.GET['id1'];
            content['User'] = Userid;
            if request.GET['id2'] and request.GET['id3']:
                Id2 = request.GET['id2'];
                Id3 = request.GET['id3'];
                if(not Lesson.objects.filter(id1 = Id2, id2 = Id3)):
                    les = Lesson(id1 = Id2, id2 = Id3);
                    les.save();
                else:
                    les = Lesson.objects.get(id1 = Id2, id2 = Id3);

                data1 = UserPlus.objects.get(userid = Userid);
                data1.lessons.add(les);
                data1.save();
                flag = True;
    content['res'] = flag;
    return render(request, 'main.html', content);

def test(request):
    return render(request, 'main.html');

def addlesson(request):
    content = {};
    #if request.GET['id1']:
    content['test'] = request.GET['id1'];
    return render(request, 'test.html', content);
    #return HttpResponse('233');

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/');
