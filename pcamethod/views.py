# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from pcamethod import main

def home(request):
    response = {}
    
    ori_shape,pca_shape,pca_num,clus_num,result_pca_kmeans,result_kmeans,labels_pca_kmeans,labels_kmeans = main.returnAPI()
    
    response['ori_shape'] = ori_shape
    response['pca_shape'] = pca_shape
    response['pca_num'] = pca_num
    response['clus_num'] = clus_num

    response['labels_pca_kmeans'] = labels_pca_kmeans
    response['labels_kmeans'] = labels_kmeans

    response['image_origin'] = "/media/origin.jpg"
    response['image_pca_kmeans'] = "/media/" + result_pca_kmeans
    response['image_kmeans'] = "/media/" + result_kmeans

    print(response['image_pca_kmeans'])

    return render(request, 'home.html', response)