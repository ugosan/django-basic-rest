from rest_framework import serializers


class PetActivitySerializer(serializers.Serializer): 
    date = serializers.DateTimeField()
    activity = serializers.CharField()
    
    
class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    creation_date = serializers.DateTimeField()
    race = serializers.CharField()
    activities = PetActivitySerializer(many=True)

