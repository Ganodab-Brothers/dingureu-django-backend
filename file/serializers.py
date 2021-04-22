from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    object_name = serializers.CharField(required=True,
                                        read_only=False,
                                        write_only=True)
    url = serializers.CharField(read_only=True)
    fields = serializers.DictField(read_only=True)