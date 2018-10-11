from django.contrib import admin
from .models import Zone, SensorType, ActionType, Sensor, Action, WeeklyProgram, Unit

admin.site.register(Zone)
admin.site.register(SensorType)
admin.site.register(ActionType)
admin.site.register(Sensor)
admin.site.register(Action)
admin.site.register(WeeklyProgram)
admin.site.register(Unit)
