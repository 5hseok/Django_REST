from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404 # get_object_or_404 불러오기
from .models import Book
from .serializers import BookSerializer

#함수형 View
@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world!")

@api_view(['GET','POST'])       # GET, POST 요청에 대해서 처리하겠다.
def booksAPI(request):          #/book/
    if request.method == 'GET': #GET 요청이면 전체 도서 정보
        books = Book.objects.all()  # Book 모델로부터 모든 도서 정보를 가져온다.
        serializer = BookSerializer(books, many=True)    #시리얼라이저에 전체 데이터를 한번에 집어넣기(직렬화, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)    # return Response
    elif request.method == 'POST':  #POST 요청이면 새로운 도서 정보 추가
        serializer = BookSerializer(data = request.data)    #POST 요청으로 들어온 데이터를 시리얼라이저에 집어넣기
        if serializer.is_valid():    #유효한 데이터라면
            serializer.save()    #시리얼라이저의 역직렬화를 통해 save(), 모델 시리얼라이저의 기본 create() 메소드가 동작
            return Response(serializer.data, status=status.HTTP_201_CREATED) #201메세지를 보내며 성공
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) #400 잘못된 요청(유효하지 않으므로)
    
@api_view(['GET'])
def bookAPI(request, bid): #/book/bid/
    book = get_object_or_404(Book, bid=bid) #bid = id인 데이터를 Book에서 가져오고 없으면 404에러
    serializer = BookSerializer(book)   #시리얼라이저에 데이터를 집어넣기(직렬화)
    return Response(serializer.data, status=status.HTTP_200_OK)   #return response
    
# 클래스형 View
class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# mixins 사용
from rest_framework import generics
from rest_framework import mixins
class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

	def get(self, request, *args, **kwargs): # GET 메소드 처리 함수(전체 목록)
		return self.list(request, *args, **kwargs)  # mixins.ListModelMixin과 연결
	def post(self, request, *args, **kwargs): # POST 메소드 처리 함수(1권 등록)
		return self.create(request, *args, **kwargs) #mixins.CreateModelMixin과 연결
class BookAPIMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'
    #django 기본 모델 pk가 아닌 bid를 pk로 사용하고 있으므로 lookup_field로 설정
    def get(self, request, *args, **kwargs):  # GET 메소드 처리 함수(1권)
        return self.retrieve(request, *args, **kwargs) #mixins.RetrieveModelMixin과 연결
    def put(self, request, *args, **kwarges): # PUT 메소드 처리 함수(1권 수정)
        return self.update(request, *args, **kwarges) # mixins.UpdateModelMixin과 연결
    def delete(self, request, *args, **kwargs): # DELETE 메소드 처리 함수(1권 삭제)
        return self.destroy(request, *args, **kwargs) # mixins.DestroyModelMixin과 연결
    
from rest_framework import generics

class BooksAPIGenerics(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookAPIGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'