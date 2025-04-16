from rest_framework.exceptions import NotAcceptable

from common.serializers import CustomSerializer
from user.models import *



class ProductSerializer(CustomSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class FeedbackSerializer(CustomSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class UserSerializer(CustomSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create_obj(self, validated_data):

        phone = validated_data.get('phone', None)

        if phone is not None:
            try:
                user = User.objects.get(phone=phone)

                return user
            except:
                # print('asd')
                return User.objects.create(phone=phone)

        else:
            raise NotAcceptable(detail=str('Phone No Not Found !'))
