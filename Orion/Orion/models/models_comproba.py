# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.forms import model_to_dict

class Comproba(models.Model):
    codcomp = models.CharField(db_column='CODCOMP', primary_key=True, max_length=3)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=80)  # Field name made lowercase.

    #def __str__(self):
       # return self.codcomp

    def toJSON(self):
        item = model_to_dict(self)
        return item

    #class Meta:
        #managed = False
    #    db_table = 'comproba'
    #    verbose_name = 'Comprobante'
    #    verbose_name_plural = 'Comprobantes'
    #    ordering = ['codcomp']

    class Meta:
        managed = False
        db_table = 'comproba'
        #ordering = ['codcomp']
