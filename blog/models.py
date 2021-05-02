from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# class PostQuerySet(models.QuerySet):
#     def genrefilter(self, genre):
#         return self.filter(genre__item = genre)

# class PostManager(models.Manager):
#     def get_queryset(self):
#         return PostQuerySet(self.model, using=self._db)

#     def genrefilter(self, genre):
#         return self.get_queryset().genrefilter(genre)

TRUE_FALSE_CHOICES = (
    ("Y", 'Yes'),
    ("N", 'No')
    )

class Post(models.Model):
  
    medium =                models.CharField(db_column='Medium', max_length=50, blank=True, null=True, default = "Movie")  # Field name made lowercase.
    name =                  models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    author_director_draw =  models.CharField(db_column='Author_Director_Draw', max_length=50, blank=True, null=True)  # Field name made lowercase.
    genre =                 models.CharField(db_column='Genre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    runtime =               models.IntegerField(db_column='Runtime', blank=True, null=True)  # Field name made lowercase.
    year_made =             models.IntegerField(db_column='Year_made', blank=True, null=True)  # Field name made lowercase.
    status =                models.CharField(db_column='Status', max_length=50, blank=True, null=True,  default = "Completed")  # Field name made lowercase.
    recommended_by =        models.CharField(db_column='Recommended_by', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date_finished =         models.DateField(db_column='Date_Finished', blank=True, null=True)  # Field name made lowercase.
    synopsis =              models.TextField(db_column='Synopsis', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    review =                models.TextField(db_column='Review', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rating =                models.SmallIntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    recommend =             models.CharField(db_column='Recommend', max_length=50, choices=TRUE_FALSE_CHOICES, blank=True, null=True, default = "Y")
    times_watched =         models.SmallIntegerField(db_column='Times_Watched', blank=True, null=True, default = 1)  # Field name made lowercase.

    # objects = PostManager()

    date_posted = models.DateTimeField( default = timezone.now)
    # # date posted auto, but you can't change the posted date
    # # date_posted = models.DateTimeField( auto_now_add = True)
    # author = models.ForeignKey(User, on_delete= models.CASCADE)
    # on_delete = CASCADE deletes all posts by a user if the user is deleted

    class Meta:
        managed = False
        db_table = 'Media'

    def __str__(self):
        return self.name, self.medium, self.genre, self.rating, self.recommend 

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    

    # ['medium','name','author_director_draw','genre','runtime','year_made','status','recommended_by','date_finished','synopsis','review','rating','times_watched']