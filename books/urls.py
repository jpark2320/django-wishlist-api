from django.urls import path
from .views import BookListView, BookCreateView, BookDeleteView

urlpatterns = [
    path('<slug>/delete', BookDeleteView.as_view()),
    path('new', BookCreateView.as_view()),
    path('', BookListView.as_view()),
]
