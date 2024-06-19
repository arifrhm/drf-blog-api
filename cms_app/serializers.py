from rest_framework import serializers
from cms_app.models import Post, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'post', 'image', 'description')
        read_only_fields = ('id',)


class PostSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'published_date', 'images')
        read_only_fields = ('id', 'published_date')
