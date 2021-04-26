from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from user.views import UserView
from file.views import FileView
from article.views import SchoolArticleView, LocalArticleView, SchoolArticleCommentView, LocalArticleCommentView

router = DefaultRouter()
router.register(r'users', UserView, basename="user")
router.register(r'files', FileView, basename="file")
router.register(
    r'articles/school',
    SchoolArticleView,
    basename="school_article",
)
router.register(
    r'articles/local',
    LocalArticleView,
    basename="local_article",
)
router.register(
    r'comments/school',
    SchoolArticleCommentView,
    basename="school_article_comment",
)
router.register(
    r'comments/local',
    LocalArticleCommentView,
    basename="local_article_comment",
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
]

urlpatterns += router.urls