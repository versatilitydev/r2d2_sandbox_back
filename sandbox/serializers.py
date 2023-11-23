from rest_framework import serializers
from .models import FILE_HASHES

class FileHashSerializer(serializers.ModelSerializer):
    class Meta:
        model = FILE_HASHES
        fields = ('id', 'file_name', 'file_hash')
