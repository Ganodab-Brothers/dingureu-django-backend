from django.db import models
from dingureu.settings import AUTH_USER_MODEL
from user.models import School


class SchoolArticle(models.Model):
    writer = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(max_length=50, null=False)
    content = models.TextField(null=False)
    school = models.ForeignKey(School, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.title


class LocalArticle(models.Model):
    writer = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(max_length=50, null=False)
    content = models.TextField(null=False)
    location = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.title


class SchoolArticleComment(models.Model):
    writer = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    article = models.OneToOneField(
        SchoolArticle,
        on_delete=models.CASCADE,
        null=False,
    )
    content = models.TextField(null=False)


class LocalArticleComment(models.Model):
    writer = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    article = models.OneToOneField(
        LocalArticle,
        on_delete=models.CASCADE,
        null=False,
    )
    content = models.TextField(null=False)