from rest_framework import serializers


class TodoCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField(required=False)
    is_complete = serializers.BooleanField()