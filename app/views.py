import pandas as pd
import numpy as np
from django.http import HttpResponse
from django.shortcuts import render, redirect
from sentence_transformers import SentenceTransformer,util
import joblib



def home(request):
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
    dic = {'list': list[:30]}

    return render(request, 'home.html', dic)


