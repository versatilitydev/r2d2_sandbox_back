from rest_framework import generics
from .models import FILE_HASHES
from .serializers import FileHashSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils import sha256_hash


@api_view(['POST'])
def getHashOfFile(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        data = request.data
        if file:
            file_name = file.name

            # Check if a file with the same name already exists
            existing_file = FILE_HASHES.objects.filter(file_name=file_name).first()
            if existing_file:
                # File with the same name exists, return an error or existing hash
                return Response({'error': 'File with this name already exists', 'hash': existing_file.file_hash},
                                status=status.HTTP_400_BAD_REQUEST)

            file_hash = sha256_hash(file)

            # Extract additional fields from request data
            vendor = data.get('vendor', '')
            product = data.get('product', '')
            version = data.get('version', '')
            update = data.get('update', '')
            language = data.get('language', '')
            edition = data.get('edition', '')
            checked = data.get('checked', False)

            # Create a new entry with all fields
            new_file = FILE_HASHES.objects.create(
                file_name=file_name, 
                file_hash=file_hash, 
                vendor=vendor, 
                product=product, 
                version=version, 
                update=update, 
                language=language, 
                edition=edition, 
                checked=checked
            )
            return Response({'file_name': new_file.file_name, 'hash': new_file.file_hash}, 
                            status=status.HTTP_201_CREATED)

        else:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def checkIfFileExists(request):
    if request.method == 'GET':
        file_name = request.GET.get('file_name')
        if file_name:
            # Check if a file with the same name already exists
            existing_file = FILE_HASHES.objects.filter(file_name=file_name).first()
            if existing_file:
                # File with the same name exists, return an error or existing hash
                return Response({'file_name': existing_file.file_name, 'hash': existing_file.file_hash},
                                status=status.HTTP_200_OK)
            else:
                return Response({'file_name': 'File with this name does not exist'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No file name provided'}, status=status.HTTP_400_BAD_REQUEST)
        

class FileHashList(generics.ListAPIView):
    queryset = FILE_HASHES.objects.all()
    serializer_class = FileHashSerializer



