from django.urls import path
from blog.api.veiwsets import ArticleListCreateAPIView , ArticleRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('list' , ArticleListCreateAPIView.as_view() , name = 'api_list'),
    path('<int:pk>', ArticleRetrieveUpdateDestroyAPIView.as_view(), name= 'api_retrive'),
]