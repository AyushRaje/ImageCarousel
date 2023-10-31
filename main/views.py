from django.shortcuts import render,redirect
import pandas as pd
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib.auth.decorators import login_required
from main.models import Feedback,Choice
from django.templatetags.static import static
import ast
# Create your views here.
increment=0

@login_required(login_url='login')
def index(request,i=0):
    print(request.user)
    data=pd.read_csv(r'static/all_images_results_new.csv')
    allennlp_data=pd.read_csv(r'static/allennlp_results.csv')
    ent_data=allennlp_data['allennlp_entities'].to_list()
    ext_ent_data=allennlp_data['extracted_entities'].to_list()
    image_data=allennlp_data['image_urls']
    image_lists=image_data.apply(ast.literal_eval).to_list()
    resultant_list=[]
    print(ent_data)
    print(ext_ent_data)
    for m in image_lists:
        new_list=[]
        for j in m:
           for k in j:
                new_list.append(k)
        resultant_list.append(new_list)
    
    context={
        'question':data['question'][i],
        'old_images':data['old_images'][i],
        'allmini_images':data['allmini_images'][i],
        'baai_images':data['baai_images'][i],
        'old_entities':data['old_entities'][i],
        'allmini_entities':data['allmini_entities'][i],
        'baai_entities':data['baai_entities'][i],
        'increment':int(i),
        'answer':data['answer'][i]
    }
    old_img=context['old_images'][1:len(context['old_images'])-1]
    allmini_img=context['allmini_images'][1:len(context['allmini_images'])-1]
    baai_img=context['baai_images'][1:len(context['baai_images'])-1]
    old_entities=context['old_entities'][1:len(context['old_entities'])-1]
    allmini_entities=context['allmini_entities'][1:len(context['allmini_entities'])-1]
    baai_entities=context['baai_entities'][1:len(context['baai_entities'])-1]
    data={
        'question':context['question'],
        'old_images':list(old_img.split(',')),
        'allmini_images':list(allmini_img.split(',')),
        'baai_images':list(baai_img.split(',')),
        'increment':int(i),
        'answer':context['answer'],
        'old_entities':list(set(old_entities.split(','))),
        'allmini_entities':list(set(allmini_entities.split(','))),
        'baai_entities':list(set(baai_entities.split(','))),
        'extracted_entities':ext_ent_data[i],
        'allennlp_entities':ent_data[i],
        'allennlp_images':resultant_list[i]

    }
    print(data)
    increment=i
    return render(request,'index.html',data)

@login_required(login_url='login')
def vote(request,i):
    data=pd.read_csv(r'static/all_images_results_new.csv')
    if request.method=='POST':

        choices=request.POST.getlist('answer')
        
        feedback=Feedback.objects.create(user=request.user)
        feedback.question=data['question'][i]
        for choice in choices:
            choice_to_add=Choice.objects.get(name=choice)
            feedback.selections.add(choice_to_add)
            feedback.save()
              
        print(choices)
    return redirect('index',i+1)

def login(request):
    if request.method=='POST':
       username=request.POST.get('username','')
       users=User.objects.all()
       for user in users:
            if user.username == username:
                authenticate(user)
                login_user(request,user=user)
                return redirect('index',0)
       
       new_user=User.objects.create_user(username=username,password='yozu')
       authenticate(new_user)
       login_user(request,user=new_user)
       return redirect('index',0)
    
    return render(request,'login.html')
def logout(request):
    logout_user(request)
    return redirect('login')



    
if __name__=='__main__':
    index()