from rest_framework.routers import DefaultRouter
from user.views import UserView

router = DefaultRouter()
router.register(r'users', UserView, basename="user")

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
]

urlpatterns += router.urls