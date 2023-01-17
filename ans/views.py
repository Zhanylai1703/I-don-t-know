from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, Question
from .serializers import CategorySerializer, QuestionSerializer
# Create your views here.


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


    
