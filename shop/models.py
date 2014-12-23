from django.db import models
from django.contrib import admin
class Post(models.Model):
	title = models.CharField(max_length = 140)
	body = models.TextField()
	description = models.TextField(blank = True)
	date = models.DateTimeField(blank = True)
	photo = models.ImageField(upload_to='upload/', blank=True)
	def __unicode(self):
		return self.title
		
class Image(models.Model):
    Post = models.ForeignKey(Post)
    image = models.ImageField()
	
class InlineImage(admin.TabularInline):
    model = Image
	
class PostAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

