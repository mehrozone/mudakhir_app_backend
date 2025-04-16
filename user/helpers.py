# from django.db.models import Q
# from rest_framework.exceptions import NotAcceptable
#
# from user.models import Department, User, Notification
#
#
# def department_filter(self, request):
#     token = request.query_params.get('token')
#     # category = request.query_params.get('category')
#     # department_type = request.query_params.get('department_type')
#     department_qf = Q()
#     if token:
#         department_qf &= (
#                 Q(title__icontains=token) |
#                 Q(description__icontains=token))
#
#     # if category:
#     #     department_qf &= Q(category_id=int(category))
#     #
#     # if department_type:
#     #     department_qf &= Q(department_type_id=int(department_type))
#
#     department_qs = Department.objects.filter(department_qf)
#     return department_qs
#
#
# def notification_filter(self, request):
#     token = request.query_params.get('department')
#     if token:
#         department_qs = Notification.objects.filter(department_id=token)
#     else:
#         department_qs = Notification.objects.all()
#
#     return department_qs
#
#
# def user_filter(self, request):
#     office_id_no = request.query_params.get('office_id_no')
#     password = request.query_params.get('password')
#     if office_id_no is None or password is None:
#         return User.objects.all()
#     else:
#         users = User.objects.filter(office_id_no=office_id_no, password=password)
#         if len(users) < 1:
#             raise NotAcceptable(detail=str('Invalid Credentials !'))
#         else:
#             return users
from user.models import Product


def product_filter(self, request):
    token = request.query_params.get('token')

    if token is None:
        return Product.objects.all()
    else:
        return Product.objects.filter(name__contains=token)
