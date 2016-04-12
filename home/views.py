from home.forms import  UserProfileForm
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.template import Template, Context
from home.models import Question_ans_key,UserProfile,Submission
import datetime,time
def home_page(request):
       hk="offline"
       if "username" in request.session:
            hk="online"
            username=request.session["username"]
            user=UserProfile.objects.get(username=username)
            current_q_no=user.current_q_no
            key=Question_ans_key.objects.get(q_no=current_q_no)
            maindata={'username':username,'hk':hk,'key':key.key,'current_q_no':current_q_no}
            context=RequestContext(request,maindata)
            return render_to_response('home/home_page.html',context)

       else:
	  	context=RequestContext(request)
      		return render_to_response('home/home_page.html',context)

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)
    registered = False
    profile_form = UserProfileForm()
    if request.method == 'POST':
        #user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if  profile_form.is_valid():
            #user = user_form.save()
            #user.set_password(user.password)
            #user.save()
            profile = profile_form.save(commit=False)
            #profile.user = user
            profile.save()
            registered = True
            username=request.POST["username"]
            request.session["username"]=username
            return HttpResponseRedirect('/home/')

        else:
            print  profile_form.errors
            return render_to_response(
                'home/register.html',
                { 'profile_form': profile_form, 'registered': registered},
                context)

    else:
        return render_to_response(
                'home/register.html',
                { 'profile_form': profile_form, 'registered': registered},
                context)

def user_login(request):
    context = RequestContext(request)
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
         
        if UserProfile.objects.get(username=username,password=password):
                user=UserProfile.objects.get(username=username,password=password)
                request.session["username"]=user.username
                return HttpResponseRedirect('/home/')
        else:
        
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('home/login.html', {}, context)
def submit_ans(request):
    if request.method=='POST':
        ans=request.POST['ans']
        wrong="1"
        username=request.session["username"]
        user=UserProfile.objects.get(username=username)
        current_q_no=user.current_q_no
        ans_retrieve=Question_ans_key.objects.get(q_no=current_q_no).ans
        #print ans,ans_retrieve
        if  ans==ans_retrieve:
            wrong="0"
            a=int(current_q_no)
            a=a+1
            user.current_q_no=a
            s=Submission()
            s.user_id=12
            s.user=user
            s.qno=a
            s.save()
            user.lst=time.time()
            user.panilty=0
            user.save()
        else:
            user.panilty=int(user.panilty)+1
            user.save()
        return HttpResponseRedirect("/home/")   


def logout(request):
    del request.session["username"]
    return HttpResponseRedirect('/home/')
def user_profile(request):
    context=RequestContext(request)
    return render_to_response('home/1.html',{},context)

def hkt(t):
    return datetime.datetime.fromtimestamp(t).strftime('%H:%M:%S')

def dashboard(request):

    obj=UserProfile.objects.order_by("-current_q_no","panilty","lst")
    str1="<table id=t01 style='width:50%'><tr><th>Rank</th><th>TeamName</th><th>Score</th></th><th>Penalty</th><th>SubmissionTime</th></tr>"
    id1=1
    for id1,user in enumerate(obj):

        str1+="<tr><td>"+str(id1)+"</td><td>"+user.username+"</td><td>"+user.current_q_no+"</td><td>"+user.panilty+"</td><td>"+str(hkt(user.lst))+"</td></tr>"
    str1+="</table>"
    return HttpResponse(str1)
                                                 
                                                    
                                                    
                                                    
                                                    