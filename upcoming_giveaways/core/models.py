from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	pdf = models.FileField(upload_to='books/pdf')
	cover = models.ImageField(upload_to='books/covers/',null=True,blank=True)

	def __str__(self):
		return self.title

	def delete(self,*args,**kwargs):
		self.pdf.delete()
		self.cover.delete()
		super().delete(*args,**kwargs)

STATUS_TYPE = (
    ('open','OPEN'),
    ('close', 'CLOSE'),
)
CATEGORY = (
    ('other','Other'),
	('mobile','Mobile'),
	('technology','Technology'),
	('electronic','Electronic'),
	('gaming','Gaming'),
	('how_to','Howto'),
	('sports','Sports'),
	('software','Software'),
	('hardware','Hardware'),
	('coupan','Coupan'),
	('quiz','Quiz'),
	('education','Education'),
)

class Giveaways (models.Model):
	logo = models.ImageField(upload_to='books/covers/',null=True,blank=True)
	name = models.CharField(max_length=100)
	status = models.CharField(max_length=6, choices=STATUS_TYPE, default='open')
	giveaways_category = models.CharField(max_length=60, choices=CATEGORY, default='other')
	product_name = models.CharField(max_length=100)
	unit = models.IntegerField(default=0)
	start_date = models.DateField()
	end_date = models.DateField()
	details = models.CharField(max_length=1000)
	links = models.URLField(max_length = 200) 
	winner_name = models.CharField(max_length=100)

	def __str__(self):
		return self.name