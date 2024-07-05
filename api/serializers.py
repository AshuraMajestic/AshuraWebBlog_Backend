from rest_framework import serializers
from .models import *


class BlogPostSerializerWithData(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = (
            "id",
            "title",
            "introduction",
            "content",
            "date",
            "minutes",
            "username",
        )

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        exclude = ['content']