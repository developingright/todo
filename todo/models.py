from typing import DefaultDict
from django.db import models
from django.contrib import admin
from django.db.models.fields import BooleanField, CharField

# Create your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ("title", "completed")
class Task(models.Model):
    title = CharField(max_length=200)
    completed = BooleanField(default=False)

    def __str__(self):
        return self.title