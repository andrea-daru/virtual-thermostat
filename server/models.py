# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.


class SensorType(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=250)


class ActionType(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=250)


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    sensorType = models.ForeignKey(SensorType, on_delete=models.CASCADE, default=None, blank=True, null=True)
    mqtt_topic = models.CharField(max_length=500, default=None, blank=True, null=True)


class SensorLog(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=2)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, default=None, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)


class Action(models.Model):
    name = models.CharField(max_length=50)
    actionType = models.ForeignKey(ActionType, on_delete=models.CASCADE, default=None, blank=True, null=True)
    mqtt_topic = models.CharField(max_length=500, default=None, blank=True, null=True)
    mqtt_payload_on = models.CharField(max_length=500, default=None, blank=True, null=True)
    mqtt_payload_off = models.CharField(max_length=500, default=None, blank=True, null=True)


class ActionLog(models.Model):
    value = models.CharField(max_length=50)
    action = models.ForeignKey(Action, on_delete=models.CASCADE, default=None, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)


class Unit(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, default=None, blank=True, null=True)
    action = models.ForeignKey(Action, on_delete=models.CASCADE, default=None, blank=True, null=True)


class WeeklyProgram(models.Model):
    name = models.CharField(max_length=50)
    sunday = JSONField(default=None, blank=True, null=True)
    monday = JSONField(default=None, blank=True, null=True)
    tuesday = JSONField(default=None, blank=True, null=True)
    wednesday = JSONField(default=None, blank=True, null=True)
    thursday = JSONField(default=None, blank=True, null=True)
    friday = JSONField(default=None, blank=True, null=True)
    saturday = JSONField(default=None, blank=True, null=True)


class Zone(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, default=None, blank=True, null=True)
    actionType = models.ForeignKey(ActionType, on_delete=models.CASCADE, default=None, blank=True, null=True)
    weeklyProgram = models.ForeignKey(WeeklyProgram, on_delete=models.CASCADE, default=None, blank=True, null=True)
