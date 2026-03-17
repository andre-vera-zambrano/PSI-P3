from rest_framework.routers import DefaultRouter
from .views import SongViewSet, SongUserViewSet
# from django . urls import path , include

router = DefaultRouter()
router.register(r'songs', SongViewSet, basename = 'songs')
router.register(r'songusers', SongUserViewSet, basename = 'songusers')

urlpatterns = []
urlpatterns += router.urls