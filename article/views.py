from django.http.request import HttpRequest
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions, status, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from article.models import LocalArticleComment, SchoolArticle, LocalArticle, SchoolArticleComment
from article.permissions import IsSameLocation, IsSameSchool, IsWriterOrReadOnly
from article.serializers import LocalArticleSerializerRetrieverDocument, SchoolArticleCommentSerializer, LocalArticleCommentSerializer, SchoolArticleSerializer, LocalArticleSerializer, SchoolArticleSerializerRetrieverDocument


class SchoolArticleCommentView(
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet,
):
    queryset = SchoolArticleComment.objects.all()
    serializer_class = SchoolArticleCommentSerializer
    permission_classes = (permissions.IsAuthenticated, IsWriterOrReadOnly)


class LocalArticleCommentView(
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet,
):
    queryset = LocalArticleComment.objects.all()
    serializer_class = LocalArticleCommentSerializer
    permission_classes = (permissions.IsAuthenticated, IsWriterOrReadOnly)


class SchoolArticleView(viewsets.ModelViewSet):
    queryset = SchoolArticle.objects.all()
    permission_classes = (
        permissions.IsAuthenticated,
        IsSameSchool,
        IsWriterOrReadOnly,
    )
    serializer_class = SchoolArticleSerializer

    def list(self, request: HttpRequest, *args, **kwargs):
        queryset = SchoolArticle.objects.filter(school=request.user.school)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request: HttpRequest, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        school = user.school
        serializer.save(
            writer=user,
            school=school,
        )
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    @swagger_auto_schema(responses={
        200: SchoolArticleSerializerRetrieverDocument,
        401: "Unauthorized"
    })
    def retrieve(self, request: HttpRequest, *args, **kwargs):
        instance = self.get_object()
        serializer: SchoolArticleSerializer = self.get_serializer(instance)
        article = serializer.data

        # get comments here
        comments = SchoolArticleComment.objects.filter(article=article['id'])
        commentSerializer: SchoolArticleCommentSerializer = SchoolArticleCommentSerializer(
            data=comments,
            many=True,
        )
        commentSerializer.is_valid()
        comments = commentSerializer.data
        comments['length'] = len(comments)
        response_body = {
            'article': article,
            'comments': comments,
        }
        return Response(response_body)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={},
        ),
        responses={
            200: SchoolArticleSerializer,
            401: "Unauthorized"
        },
    )
    @action(detail=True, methods=['POST'])
    def heart(self, request: HttpRequest, pk=None):
        article = get_object_or_404(SchoolArticle, id=pk)
        if request.user in article.hearts.all():  # remove heart
            article.hearts.remove(request.user)
        else:
            article.hearts.add(request.user)
        serializer: SchoolArticleSerializer = self.get_serializer(article)
        return Response(serializer.data)


class LocalArticleView(viewsets.ModelViewSet):
    queryset = LocalArticle.objects.all()
    permission_classes = (
        permissions.IsAuthenticated,
        IsSameLocation,
        IsWriterOrReadOnly,
    )
    serializer_class = LocalArticleSerializer

    def list(self, request: HttpRequest, *args, **kwargs):
        queryset = LocalArticle.objects.filter(location=request.user.location)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request: HttpRequest, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        school = user.school
        location = school.location
        serializer.save(
            writer=user,
            school=school,
            location=location,
        )
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    @swagger_auto_schema(
        responses={
            200: LocalArticleSerializerRetrieverDocument,
            401: "Unauthorized",
        }, )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer: LocalArticleSerializer = self.get_serializer(instance)
        article = serializer.data

        comments = LocalArticleComment.objects.filter(article=article['id'])
        commentSerializer: LocalArticleCommentSerializer = LocalArticleCommentSerializer(
            data=comments,
            many=True,
        )
        commentSerializer.is_valid()
        response_body = {
            'article': article,
            'comments': commentSerializer.data
        }
        return Response(response_body)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={},
        ),
        responses={
            200: LocalArticleSerializer,
            401: "Unauthorized"
        },
    )
    @action(detail=True, methods=['POST'])
    def heart(self, request: HttpRequest, pk=None):
        article = get_object_or_404(LocalArticle, id=pk)
        if request.user in article.hearts.all():  # remove heart
            article.hearts.remove(request.user)
        else:
            article.hearts.add(request.user)
        serializer: LocalArticleSerializer = self.get_serializer(article)
        return Response(serializer.data)