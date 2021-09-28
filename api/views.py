#from django.shortcuts import render
from .serializers import DocumentSerializer
from documents.models import Document
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from wsgiref.util import FileWrapper

class FileReadView(APIView):
    def get(self, request, id=None):
        if id:
            file = Document.objects.get(id=id)
            serializer = DocumentSerializer(file)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        file = Document.objects.all()
        serializer = DocumentSerializer(file, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class FileDownloadView(APIView):
    def get(self, request, id, format=None):
        queryset = Document.objects.get(id=id)
        queryset.increment_nrDownloads()
        file_handle = queryset.file.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/msword')
        response['Content-Disposition'] = 'attachment; filename="%s"' % queryset.file.name
        return response

class FileWriteView(APIView):
    def put(self, request, *args, **kwargs):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id=None):
        item = get_object_or_404(Document, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})

