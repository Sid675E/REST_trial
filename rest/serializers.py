from rest_framework import serializers
from .models import table_rest

class table_restSerializer(serializers.ModelSerializer):

    class Meta:
        model = table_rest
        fields = '__all__'