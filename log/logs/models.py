from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Topic(models.Model):
    text = models.CharField(max_length=200)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Person(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()
    father_name = models.TextField()
    born_date = models.TextField()
    garage_number = models.IntegerField()
    phone_number = models.IntegerField()
    e_mail = models.EmailField()
    address = models.TextField()
    counter_model = models.TextField()
    cuonter_number = models.TextField()
    counter_install_date = models.TextField()
    counter_expluatation_end_date = models.TextField()
    counter_install_start_data = models.IntegerField()
    counter_expluatation_end_data = models.IntegerField()
    # courses = models.ManyToManyField("Course", blank=True)
    # class Meta:
    #     verbose_name_plural = "People"

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)

    text = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + "..."