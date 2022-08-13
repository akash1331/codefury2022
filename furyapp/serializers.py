from rest_framework import serializers
from furyapp.models import *

# class startup_userSerializer(serializers.ModelSerializer):
#     class Meta():
#         model = usertype
#         fields = '__all__'

class inverstorsSerializer(serializers.ModelSerializer):
    class Meta():
        model = investors
        fields = '__all__'

class startup_dataSerializer(serializers.ModelSerializer):
    class Meta():
        model = startup_data
        fields = '__all__'

class startup_postSerializer(serializers.ModelSerializer):
    class Meta():
        model = startup_post
        fields = '__all__'