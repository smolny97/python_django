from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics,viewsets,mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from .serializers import *
from .models import *
import requests

class GamesViewSet(mixins.CreateModelMixin,
						 mixins.RetrieveModelMixin,
						 mixins.UpdateModelMixin,
						 mixins.ListModelMixin,
						 GenericViewSet,):
	queryset = Games.objects.all()
	serializer_class = GamesSerializer
	@action(methods=['get'],detail=True)
	def category(self, request, pk=None):
		name = Games.objects.get(pk=pk)
		return Response({'name':name.name_game})
class GameViewSet(mixins.CreateModelMixin,
						 mixins.RetrieveModelMixin,
						 mixins.UpdateModelMixin,
						 mixins.ListModelMixin,
						 GenericViewSet,):
	queryset = Game.objects.all()
	serializer_class = GameSerializer
	@action(methods=['get'],detail=True)
	def category(self, request, pk=None):
		name = Game.objects.get(pk=pk)
		return Response({'name':name.name_game})
class BlogViewSet(mixins.CreateModelMixin,
						 mixins.RetrieveModelMixin,
						 mixins.UpdateModelMixin,
						 mixins.ListModelMixin,
						 GenericViewSet,):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer
	@action(methods=['get'],detail=True)
	def category(self, request, pk=None):
		text = Blog.objects.get(pk=pk)
		return Response({'text':text.text_game})
# Create your Gam here.
def index(request):
	#requests.put("http://127.0.0.1:8000/api/v1/main/9/", data= {"text_game": "rtb", "name_game": "ssd","link_game": "svg","img_game": "sg"})
	#df = requests.get("http://127.0.0.1:8000/api/v1/main/").json()
	#data = {'data':df}
	return render(request,'index.html')
def about(request):
	return render(request,'about.html')
def user_agreement(request):
	return render(request,'user_agreement.html')
def privacy_policy(request):
	return render(request,'privacy_policy.html')
def games(request):
	#if(request.POST.get('mybtn')):
		#return render(request,'game.html')
	data={'games':Games.objects.all()}
	return render(request,'games.html',data)
def blog(request):
	data={'blog':Blog.objects.all()}
	return render(request,'blog.html',data)
def game(request,name_game):	
	data={
		'picture_banner': "images/"+name_game+"/2.jpg",
		'picture_video': "images/"+name_game+"/3.jpg",
		'picture_info': "images/"+name_game+"/4.jpg",
		'picture1': "images/"+name_game+"/1.jpg",
		'picture2': "images/"+name_game+"/2.jpg",
		'picture3': "images/"+name_game+"/3.jpg",
		'picture4': "images/"+name_game+"/4.jpg",
		'picture5': "images/"+name_game+"/5.jpg",
		'picture6': "images/"+name_game+"/6.jpg",
		'picture7': "images/"+name_game+"/7.jpg",
		'picture8': "images/"+name_game+"/8.jpg",
		'name_game':Game.objects.filter(name_game__contains=name_game)[0]
	}	
	return render(request,'game.html',data)