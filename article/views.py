from django.http.request import HttpRequest
from rest_framework import viewsets, permissions, status, mixins
from rest_framework.response import Response
from article.models import LocalArticleComment, SchoolArticle, LocalArticle, SchoolArticleComment
from article.permissions import IsSameLocation, IsSameSchool, IsWriterOrReadOnly
from article.serializers import SchoolArticleCommentSerializer, LocalArticleCommentSerializer, SchoolArticleSerializer, LocalArticleSerializer


class SchoolArticleCommentView(
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
):
    queryset = SchoolArticleComment.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsWriterOrReadOnly)


class LocalArticleCommentView(
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
):
    queryset = LocalArticleComment.objects.all()
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
        serializer.save(writer=request.user, school=request.user.school)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


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
        serializer.save(writer=request.user, location=request.user.location)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )
