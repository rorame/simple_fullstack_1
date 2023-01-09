from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Books
from .serializer import BookSerializer


# class BookApiView(APIView):
#     def get(self, request):
#         output = [
#             {
#                 "title": output.title,
#                 "author": output.author
#             } for output in Books.objects.all()
#         ]
#         return Response(output)
#
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)



class BookApiList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


