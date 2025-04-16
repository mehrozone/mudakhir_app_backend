from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from common.apis import FullViewSet
from user import helpers
from user.models import *
from user.serlializers import *


class UserViewSet(FullViewSet):
    """
    API endpoint for managing users.
    
    This endpoint allows you to:
    - List all users
    - Create a new user
    - Retrieve a specific user
    - Update a user
    - Delete a user
    """
    # permission_classes = (AllowAny,)
    ObjModel = User
    ObjSerializer = UserSerializer

    @swagger_auto_schema(
        operation_description="List all users",
        responses={200: UserSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new user",
        request_body=UserSerializer,
        responses={201: UserSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class FeedbackViewSet(FullViewSet):
    """
    API endpoint for managing feedback.
    
    This endpoint allows you to:
    - List all feedback entries
    - Create new feedback
    - Retrieve specific feedback
    - Update feedback
    - Delete feedback
    """
    # permission_classes = (AllowAny,)
    ObjModel = Feedback
    ObjSerializer = FeedbackSerializer

    @swagger_auto_schema(
        operation_description="List all feedback entries",
        responses={200: FeedbackSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create new feedback",
        request_body=FeedbackSerializer,
        responses={201: FeedbackSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class ProductViewSet(FullViewSet):
    """
    API endpoint for managing products.
    
    This endpoint allows you to:
    - List all products
    - Create a new product
    - Retrieve a specific product
    - Update a product
    - Delete a product
    """
    # permission_classes = (AllowAny,)
    ObjModel = Product
    ObjSerializer = ProductSerializer

    @swagger_auto_schema(
        operation_description="List all products",
        responses={200: ProductSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new product",
        request_body=ProductSerializer,
        responses={201: ProductSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def obj_filter(self, request):
        return helpers.product_filter(self, request)
