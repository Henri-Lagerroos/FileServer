from rest_framework import serializers
from documents.models import Document

class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('id', 'title', 'file', 'timeStamp', 'nrDownloads')