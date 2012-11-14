# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource

import settings as s

# Приоритет заявки
class TaskPriority(models.Model):
    name  = models.CharField(max_length=s.TASK_PRIORITY_NAME_LENGTH, unique=True)
    
    class Meta:
        app_label = 'left'
        db_table = 'task_priority'



class Handler( ModelResource ):
    class Meta:
        queryset = TaskPriority.objects.all()
        resource_name = 'task_priority'
    