from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register', )
router.register('login', )


urlpatterns = [
   path('', include('router.urls')),

]