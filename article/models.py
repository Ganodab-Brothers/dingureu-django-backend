from django.db import models
from dingureu.settings import AUTH_USER_MODEL
from user.models import School


class SchoolArticle(models.Model):
    writer = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='writer',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, null=False)
    content = models.TextField(null=False)
    school = models.ForeignKey(School, on_delete=models.PROTECT, null=False)
    hearts = models.ManyToManyField(AUTH_USER_MODEL, related_name='hearts')

    def __str__(self):
        return self.title


class LocalArticle(models.Model):
    writer = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, null=False)
    content = models.TextField(null=False)
    school = models.ForeignKey(School, on_delete=models.PROTECT, null=False)

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