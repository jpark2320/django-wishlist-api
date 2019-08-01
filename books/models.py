from django.db import models
from django.template.defaultfilters import slugify


class TimeStampedModel(models.Model):

    class Meta:
        abstract = True

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Book(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    author = models.CharField(max_length=255)

    def __str__(self):
        return '[Book] {0} (by {1})'.format(self.title, self.author)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)
