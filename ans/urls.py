from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, QuestionViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet,basename='category')
router.register('news', QuestionViewSet,basename='news')

urlpatterns = router.urls