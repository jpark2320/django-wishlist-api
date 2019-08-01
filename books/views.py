from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from .models import Book
from .serializers import BookSerializer


class BookListView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        q = self.request.query_params.get('q', None)

        if q is not None:
            queryset = queryset.filter(title__icontains=q)

        return queryset


class BookCreateView(CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDeleteView(DestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'slug'
