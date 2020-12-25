from rest_framework import serializers


class UmpireSerializers(serializers.Serializer):
    nationality = serializers.CharField(max_length=50)
    total = serializers.IntegerField()


class TeamSerializers(serializers.Serializer):
    batting_team = serializers.CharField(max_length=50)
    dsum = serializers.IntegerField()


class BatsmanSerializers(serializers.Serializer):
    batsman = serializers.CharField(max_length=50)
    runs = serializers.IntegerField()
    # batting_team = serializers.CharField(max_length=50)


class StackedSerializers(serializers.Serializer):
    pass