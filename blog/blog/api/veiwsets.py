
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from blog.models import Article
from .serilaizer import ArticleSerilaizer
from .permission import IsOwnerOrReadOnly , permissions
# from rest_framework import permissions


class ArticleListCreateAPIView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerilaizer
    
    


class ArticleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset =  Article.objects.all()
    serializer_class = ArticleSerilaizer
    permission_classes = (IsOwnerOrReadOnly , permissions.IsAuthenticated )