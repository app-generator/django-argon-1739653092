# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Paciente(models.Model):

    #__Paciente_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    fecha de nacimiento = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Paciente_FIELDS__END

    class Meta:
        verbose_name        = _("Paciente")
        verbose_name_plural = _("Paciente")


class Historiaclinica(models.Model):

    #__Historiaclinica_FIELDS__
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    saturacion = models.IntegerField(null=True, blank=True)

    #__Historiaclinica_FIELDS__END

    class Meta:
        verbose_name        = _("Historiaclinica")
        verbose_name_plural = _("Historiaclinica")


class Archivohistoria(models.Model):

    #__Archivohistoria_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    historia = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)

    #__Archivohistoria_FIELDS__END

    class Meta:
        verbose_name        = _("Archivohistoria")
        verbose_name_plural = _("Archivohistoria")



#__MODELS__END
