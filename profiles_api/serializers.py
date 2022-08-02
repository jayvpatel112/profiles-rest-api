from rest_framework import serializers

class Helloserializer(serializers.Serializer):
    """Serialize a name field for testing purpose"""
    name = serializers.CharField(max_length=20)