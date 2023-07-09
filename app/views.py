import pandas as pd
import numpy as np
from django.http import HttpResponse
from django.shortcuts import render, redirect
from sentence_transformers import SentenceTransformer,util
import joblib
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        username_error_message = ""
        email_error_message = ""
        if User.objects.filter(username=uname).exists():
            username_error_message= "Username is already taken"
            # return render(request,'signup.html',{'username_error_messages':username_error_messages})
        if User.objects.filter(email=email).exists():
            email_error_message= "Email is already taken"
            # return render(request, 'signup.html', {'email_error_messages': email_error_messages})

        print(len(username_error_message))
        print(len(email_error_message))
        if len(username_error_message) > 0 or len(email_error_message) > 0:
            return render(request, 'signup.html', {'username_error_message': username_error_message,
                                                   'email_error_message': email_error_message})
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            login(request, my_user)
            return redirect('search')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('search')
        else:
            return render(request,'login.html',{'error_message':"Invalid Credential"})

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def SearchPage(request):
    return render(request,'search.html')


@login_required(login_url='login')
def HomePage(request):
    embeddings=joblib.load('C:/Users/pallav/PycharmProjects/Hackathon/AiSearch/app/embeddings')
    model=joblib.load('C:/Users/pallav/PycharmProjects/Hackathon/AiSearch/app/model')
    product_urls=joblib.load('C:/Users/pallav/PycharmProjects/Hackathon/AiSearch/app/product_urls')
    images=joblib.load('C:/Users/pallav/PycharmProjects/Hackathon/AiSearch/app/images')
    descriptions=joblib.load('C:/Users/pallav/PycharmProjects/Hackathon/AiSearch/app/descriptions')
    # df = pd.read_csv('C:/Users/pallav/PycharmProjects/Hackathon/AiSearch/app/abc.csv')
    texts = joblib.load('C:/Users/pallav/PycharmProjects/Hackathon/AiSearch/app/texts')
    sentences = ["tshirts"]
    name = []
    sim = []
    desc = []
    img = []
    lnk = []
    if request.method == 'POST':
        search = request.POST.get('search')
        print(search)
        sentences=[]
        sentences.append(search)
        embeddings1 = model.encode(sentences)
        cos_sim = util.cos_sim(embeddings, embeddings1)
        # name = []
        # sim = []
        # desc = []
        # img = []
        # lnk = []
        print(len(cos_sim))
        print(len(texts))
        print(len(descriptions))
        print(len(images))
        print(len(product_urls))
        for i in range(len(cos_sim)):
            # sim.append(np.asscalar(cos_sim[i][0].numpy()))
            sim.append(cos_sim[i][0].numpy().item())
            name.append(texts[i])
            desc.append(descriptions[i])
            img.append(images[i])
            lnk.append(product_urls[i])

        # dic = {'name': name, 'sim': sim, 'desc': desc, 'img': img, 'link': lnk}
        # new_df = pd.DataFrame(dic)
        # new_df = new_df.sort_values(by='sim', ascending=False)
        # # new_df=new_df.iloc[10,:]
        # list = new_df.to_dict('records')
        # # new_list=new_df.head(10)
        # dic = {'list': list[:10]}
        # return render(request, 'home.html', dic)

    # return render(request,'home.html')
    dic = {'name': name, 'sim': sim, 'desc': desc, 'img': img, 'link': lnk}
    new_df = pd.DataFrame(dic)
    new_df = new_df.sort_values(by='sim', ascending=False)
    # new_df=new_df.iloc[10,:]
    list = new_df.to_dict('records')
    # new_list=new_df.head(10)
    dic = {'list': list[:30],'request':request,'search':search}

    return render(request, 'home.html', dic)


