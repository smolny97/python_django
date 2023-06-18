from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import *

class GamesModel:
	def __init__(self,name,text):
		self.name = name
		self.text = text

class GamesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Games
		#fields = ("text_game","link_game","name_game","img_game")
		fields = ("__all__")
class GameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Game
		fields = ("__all__")
class BlogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Blog
		fields = ("__all__")

# def encode():
# 	model = GamesModel('tomas','name:tomas')
# 	model_sr = GamesSerializer(model)
# 	json = JSONRenderer().render(model_sr.data,type(model_sr.data))