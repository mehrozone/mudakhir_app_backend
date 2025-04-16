from rest_framework import routers
from django.urls import path

from user.views import *

router = routers.DefaultRouter()
router.register('user', UserViewSet, basename='user')
router.register('product', ProductViewSet, basename='product')
router.register('feedback', FeedbackViewSet, basename='feedback')
urlpatterns = [

]

urlpatterns += router.urls
