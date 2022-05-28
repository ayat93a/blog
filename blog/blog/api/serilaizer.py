from distutils.filelist import FileList
from pyexpat import model
from attr import fields
from rest_framework import serializers
from blog.models import Article


class ArticleSerilaizer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Article