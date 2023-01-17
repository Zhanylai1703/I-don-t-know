from .models import Question, Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']
        

class QuestionSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Question
        fields = ['question', 'answer', 'category']

