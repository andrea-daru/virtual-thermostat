"""vt_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers, serializers, viewsets
from server.models import Zone
from server.models import SensorType
from server.models import ActionType
from server.models import Sensor
from server.models import Action
from server.models import WeeklyProgram
from server.models import Unit
from server.models import SensorLog
from server.models import ActionLog


# Serializers define the API representation.
class SensorTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorType
        fields = ('code', 'description')


# ViewSets define the view behavior.
class SensorTypeViewSet(viewsets.ModelViewSet):
    queryset = SensorType.objects.all()
    serializer_class = SensorTypeSerializer
    

# Serializers define the API representation.
class ActionTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActionType
        fields = ('code', 'description')


# ViewSets define the view behavior.
class ActionTypeViewSet(viewsets.ModelViewSet):
    queryset = ActionType.objects.all()
    serializer_class = ActionTypeSerializer


# Serializers define the API representation.
class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('name', 'sensorType', 'mqtt_topic')


# ViewSets define the view behavior.
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
# Serializers define the API representation.
class SensorLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorLog
        fields = ('name', 'sensorType', 'mqtt_topic')


# ViewSets define the view behavior.
class SensorLogViewSet(viewsets.ModelViewSet):
    queryset = SensorLog.objects.all()
    serializer_class = SensorLogSerializer
    
# Serializers define the API representation.
class ActionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Action
        fields = ('name', 'actionType', 'mqtt_topic', 'mqtt_payload_on', 'mqtt_payload_off')


# ViewSets define the view behavior.
class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

# Serializers define the API representation.
class ActionLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActionLog
        fields = ('name', 'ActionType', 'mqtt_topic')


# ViewSets define the view behavior.
class ActionLogViewSet(viewsets.ModelViewSet):
    queryset = ActionLog.objects.all()
    serializer_class = ActionLogSerializer


# Serializers define the API representation.
class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = ('name', 'description', 'sensor', 'action')


# ViewSets define the view behavior.
class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    
    
# Serializers define the API representation.
class WeeklyProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeeklyProgram
        fields = ('name', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')


# ViewSets define the view behavior.
class WeeklyProgramViewSet(viewsets.ModelViewSet):
    queryset = WeeklyProgram.objects.all()
    serializer_class = WeeklyProgramSerializer
    

# Serializers define the API representation.
class ZoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zone
        fields = ('name', 'description', 'actionType', 'weeklyProgram')


# ViewSets define the view behavior.
class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'zones', ZoneViewSet)
router.register(r'sensor_types', SensorTypeViewSet)
router.register(r'action_types', ActionTypeViewSet)
router.register(r'sensor', SensorViewSet)
router.register(r'sensor_log', SensorLogViewSet)
router.register(r'action', ActionViewSet)
router.register(r'action_log', ActionLogViewSet)
router.register(r'weekly_program', WeeklyProgramViewSet)
router.register(r'unit', UnitViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
