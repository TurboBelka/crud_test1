from django.db import models
from django.utils import timezone


class Languages(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TourLeads(models.Model):
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    PROF_CHOICES = (
        ('y', 'Yes'),
        ('n', 'No')
    )
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='m')
    languages = models.ManyToManyField(Languages, through='TourLeadsLanguages')
    card_number = models.CharField(max_length=15, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    professional = models.CharField(max_length=1, choices=PROF_CHOICES, default='y')


class TourLeadsLanguages(models.Model):
    tourlead = models.ForeignKey(TourLeads)
    language = models.ForeignKey(Languages)
