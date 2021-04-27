from rest_framework import serializers
from article.models import SchoolArticle, LocalArticle, SchoolArticleComment, LocalArticleComment


class SchoolArticleCommentSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')

    class Meta:
        model = SchoolArticleComment
        fields = '__all__'


class LocalArticleCommentSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')

    class Meta:
        model = LocalArticleComment
        fields = '__all__'


class SchoolArticleSerializer(serializers.ModelSerializer):
    writer = serializers.SlugRelatedField(
        read_only=True,
        slug_field='nickname',
    )
    school = serializers.SlugRelatedField(
        read_only=True,
        slug_field="school_name",
    )
    created_at = serializers.DateTimeField(read_only=True)
    hearts = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field='nickname',
    )

    class Meta:
        model = SchoolArticle
        fields = '__all__'


class LocalArticleSerializer(serializers.ModelSerializer):
    writer = serializers.SlugRelatedField(
        read_only=True,
        slug_field='nickname',
    )
    school = serializers.SlugRelatedField(
        read_only=True,
        slug_field="school_name",
    )
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = LocalArticle
        fields = '__all__'


class SchoolArticleSerializerRetrieverDocument(serializers.Serializer):
    article = SchoolArticleSerializer()
    comments = SchoolArticleCommentSerializer(many=True)


class LocalArticleSerializerRetrieverDocument(serializers.Serializer):
    article = LocalArticleSerializer()
    comments = LocalArticleCommentSerializer(many=True)