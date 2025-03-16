from django.db import models
from django.utils.text import slugify

# Create your models here.
# class JobPost (models.Model):
#     title = models.CharField(max_length=30)
#     description = models.CharField(max_length=30)
#     date = models.DateTimeField(auto_now_add=True)
#     salary = models.IntegerField(default=1000)

# class JobPost(models.Model):
#     title = models.CharField(max_length=30)
#     description = models.CharField(max_length=30)
#     date = models.DateTimeField(auto_now_add=True)
#     salary = models.IntegerField()


class Skill(models.Model):
    name = models.CharField(max_length=30)


class Author(models.Model):
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)


class Location (models.Model):
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    zip = models.CharField(max_length=30)


class JobPost(models.Model):
    JOB_TYPE_CHOICES = [('Full Time', 'Full Time'), ('Part Time', 'Part Time')]
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    expiry = models.DateField(null=True)
    salary = models.IntegerField()
    slug = models.SlugField(null=True, max_length=40, unique=True)
    location = models.OneToOneField(
        Location, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    skills = models.ManyToManyField(Skill)
    type = models.CharField(max_length=200, null=False,
                            choices=JOB_TYPE_CHOICES)
    # // author can be null

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)

    # def __str__(self):
    #     return self.title

    def __str__(self):
        return f"{self.title} with Salary {self.salary}"

# class JobPost(models.Model):
#     pass
