from rest_framework import serializers
from .models import Appointment
import datetime


class AppointmentSerializer(serializers.ModelSerializer):
    ends_at = serializers.SerializerMethodField('get_ends_at')

    def get_ends_at(self, obj):
        return obj.starts_at + obj.duration

    class Meta:
        model = Appointment
        fields = '__all__'


