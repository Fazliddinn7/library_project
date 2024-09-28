from django.urls import path

from book.views import BookRetrieveUpdateDestroyAPIView, BookListCreateAPIView

urlpatterns = [
    path('books-list-create/', BookListCreateAPIView.as_view()),
    path('books-retrieve-update-destroy/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view()),
]
