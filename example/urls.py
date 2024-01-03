from django.urls import path, include
from .views import HelloAPI, bookAPI, booksAPI, BookAPI, BooksAPI, BooksAPIMixins, BookAPIMixins

urlpatterns = [
    path("hello/", HelloAPI),
    path("fbv/books/", booksAPI),
    path("fbv/book/<int:bid>/",bookAPI),
    path("cbv/books/", BooksAPI.as_view()),             # CBV의 뷰를 path에 등록할 때는 .as_view를 사용한다.
    path("cbv/book/<int:bid>/", BookAPI.as_view()),
    path("mixin/books/", BooksAPIMixins.as_view()),
    path("mixin/book/<int:bid>/", BookAPIMixins.as_view()),
]