from django.db import models
from django.conf import settings

# Create your models here.
class Games(models.Model):
	text_game = models.TextField(blank=True, null=True)
	link_game = models.TextField(blank=True, null=True)
	name_game = models.TextField(blank=True, null=True)
	img_game = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.name_game	
	class Meta:
		managed = False
		db_table = 'games'
class Blog(models.Model):
   data = models.TextField(blank=True, null=True)
   text_blog = models.TextField(blank=True, null=True)
   img_blog = models.TextField(blank=True, null=True)
   video_blog = models.TextField(blank=True, null=True)
   class Meta:
      managed = False
      db_table = 'blog'
class Game(models.Model):
   name_game = models.TextField(blank=True, null=True)
   video_game = models.TextField(blank=True, null=True)
   text_game = models.TextField(blank=True, null=True)
   class Meta:
      managed = False
      db_table = 'game'