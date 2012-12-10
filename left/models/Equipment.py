# -*- coding: utf-8 -*-

from django.db import models
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

import settings as s

# Оборудование
class Equipment(models.Model):
    name             = models.CharField(max_length=s.EQ_NAME_LENGTH)
    serial_number    = models.CharField(max_length=s.SN_NAME_LENGTH, unique=True)
    addr             = models.CharField(max_length=s.EQ_ADDR_LENGTH, null=True)
    equipment_model  = models.ForeignKey('EquipmentModel')
    owner            = models.ManyToManyField('right.Employee', through='right.EquipmentOwner')
     
    class Meta:
        app_label = 'left'
        db_table = 'equipment'
        
    def __str__(self):
        format = '[%d : %s : %s : %s : %d]'
        return format % (self.id, self.name, self.serial_number, self.addr, self.equipment_model_id)
    
    def __unicode__(self):
        return self.__str__()



import EquipmentModel
class Handler( ModelResource ):
    equipment_model_url = fields.ForeignKey(EquipmentModel.Handler, 'equipment_model')
    equipment_model_id  = fields.IntegerField('equipment_model_id')
    
    class Meta:
        queryset = Equipment.objects.all()
        resource_name = 'equipment'

    filtering = {
        'id'                : ALL,
        'name'              : ALL,
        'serial_number'     : ALL,
        'addr'              : ALL,
        'equipment_model'   : ALL_WITH_RELATIONS,
    }
