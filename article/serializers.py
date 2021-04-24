from rest_framework import serializers
from article.models import SchoolArticle, LocalArticle
from user.models import User, School


class SchoolArticleSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')
    school = serializers.ReadOnlyField()

    class Meta:
        model = SchoolArticle
        fields = '__all__'


class LocalArticleSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')
    location = serializers.ReadOnlyField()

    class Meta:
        model = LocalArticle
        fields = '__all__'