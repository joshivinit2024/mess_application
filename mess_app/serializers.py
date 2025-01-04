from rest_framework import serializers
from .models import User,Details

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'number','password']
        extra_kwargs = {'password': {'write_only': True}}
        
class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'