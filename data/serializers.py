from rest_framework import serializers
from data.models import Umpire


class UmpireSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    nationality = serializers.CharField(max_length=50)
    first_officiated = serializers.IntegerField()
    last_officiated = serializers.IntegerField()
    Number_of_Matches = serializers.IntegerField()



# class UmpireSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Umpire
#         fields = '__all__'
