from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from . models import company_details,contact

class company_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = company_details
        fields = '__all__'
class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = '__all__'