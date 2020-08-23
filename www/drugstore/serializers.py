from .models import Drug, Vaccination
from rest_framework import serializers


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = ['id', 'name', 'code', 'description']


class VaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccination
        fields = ['id', 'rut', 'dose', 'date', 'drug']
    #
    # def validate(self, attrs):
    #     attrs

    def to_representation(self, instance):
        """
        Required for foreign key
        :param instance:
        :return: self
        """
        self.fields['drug'] = DrugSerializer(read_only=True)
        return super(VaccinationSerializer, self).to_representation(instance)
