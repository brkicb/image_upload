from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Image
from .serializers import ImageSerializer


class GetImagesView(APIView):
    def get(self, request, format=None):
        if Image.objects.all().exists():
            images = Image.objects.all()
            images = ImageSerializer(images, many=True)

            return Response(
                {'images': images.data},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'error': 'No images found'},
                status=status.HTTP_404_NOT_FOUND
            )


class ImageUploadView(APIView):
    def post(self, request):
        data = self.request.data

        image = data['image']

        created_image = Image.objects.create(
            image=image,
            alt='Laptop'
        )

        print(created_image)

        return Response(
            {'success': 'Successfully uploaded image'},
            status=status.HTTP_201_CREATED
        )
