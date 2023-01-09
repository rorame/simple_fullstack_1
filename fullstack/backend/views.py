from rest_framework import generics

from .models import Books
from .serializer import BookSerializer


class BookApiList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
