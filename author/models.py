from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Author(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    date_of_b = models.DateField(null=True,blank=True)
    date_of_d = models.DateField('Died',null=True,blank=True)


    def get_absolute_url(self):
        return reverse('author:author_list',args=[str(self.id)])

    def __str__(self):

        return '{},{}'.format(self.fname,self.lname)


#
class Book(models.Model):
    COMIC = "CM"
    VICTION = "VC"
    LIST =[
        (COMIC,'Comic'),
        (VICTION,'Viction')
    ]


    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="book")
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,max_length=255)
    date = models.DateField(auto_now=True)
    published = models.CharField(max_length=5,choices=LIST,default=COMIC)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.author

