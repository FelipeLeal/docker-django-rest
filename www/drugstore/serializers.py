from .models import Drug, Vaccination
from rest_framework import serializers


class DrugSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drug
        fields = ['id', 'name', 'code', 'description']


class VaccinationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vaccination
        fields = ['id', 'rut', 'dose', 'date', 'drug']