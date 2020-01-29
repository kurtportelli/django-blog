from django.db import models


class Gender(models.Model):
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.gender


class Topic(models.Model):
    topic = models.CharField(max_length=100)

    def __str__(self):
        return self.topic


class Author(models.Model):
    full_name = models.CharField(max_length=70)
    email = models.EmailField()
    website = models.URLField(max_length=200)
    locality = models.CharField(max_length=70)
    age = models.PositiveSmallIntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('published date')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    topics = models.ManyToManyField(Topic)

    def __str__(self):
        return self.title
