# Create your models here.
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, Group as RoleModel, PermissionsMixin
from django.db import models
from django.utils import timezone

from common.models import TSFieldsIndexed


class Role(RoleModel):
    class Meta:
        proxy = True


class UserPermissionsMixin(PermissionsMixin):
    groups = None  # remove this field from super class
    user_permissions = None  # remove this field from super class

    role = models.ForeignKey(Role, null=True, on_delete=models.PROTECT)

    class Meta:
        abstract = True


class SimpleUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.is_active = False
        user.is_staff = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(TSFieldsIndexed):
    is_active = models.BooleanField(default=False)
    member = models.IntegerField(default=0,null=True)
    expense = models.TextField(default='',null=True)
    budget = models.TextField(default='',null=True)
    phone = models.CharField(max_length=120, null=True, blank=True)
    package = models.TextField(null=True, default='')
    membership_start_date = models.DateTimeField(default=timezone.now,null=True)
    name = models.TextField(default='',null=True)
    need = models.FloatField(default=0.0,null=True)
    a = models.FloatField(default=0.0,null=True)
    b = models.FloatField(default=0.0,null=True)
    ae = models.FloatField(default=0.0,null=True)
    userID = models.IntegerField(default=-1,null=True)
    fakeIncomeDate = models.DateTimeField(default=timezone.now,null=True)
    goalStart = models.DateTimeField(default=timezone.now,null=True)
    be = models.FloatField(default=0.0,null=True)
    startFrom = models.DateTimeField(default=timezone.now,null=True)
    totalBudget = models.FloatField(default=0.0,null=True)
    incomeLeft = models.FloatField(default=0.0,null=True)
    anyOtherExpenseThisMonth = models.FloatField(default=0.0,null=True)
    realExpense = models.FloatField(default=0.0,null=True)
    totalBasicexpense = models.FloatField(default=0.0,null=True)
    target = models.FloatField(default=0.0,null=True)
    goalDate = models.DateTimeField(default=timezone.now,null=True)
    projectedExpense = models.FloatField(default=0.0,null=True)
    budgetLeft = models.FloatField(default=0.0,null=True)
    email = models.TextField(default='',null=True)
    todaysBudget = models.FloatField(default=0.0,null=True)
    todaysExpense = models.FloatField(default=0.0,null=True)
    monthlyIncome = models.FloatField(default=0.0,null=True)
    currency = models.TextField(default='',null=True)
    surplus = models.FloatField(default=0.0,null=True)
    amountLeft = models.FloatField(default=0.0,null=True)
    sallaryDate = models.DateTimeField(default=timezone.now,null=True)
    weekendOne = models.FloatField(default=0.0,null=True)
    weekendTwo = models.FloatField(default=0.0,null=True)
    weekDaysBudget = models.FloatField(default=0.0,null=True)
    firstWeekendBudget = models.FloatField(default=0.0,null=True)
    secondWeekendBudget = models.FloatField(default=0.0,null=True)

    def __str__(self):
        return str(self.phone)


class Feedback(TSFieldsIndexed):
    name = models.CharField(null=True, default='', max_length=500)
    email = models.CharField(null=True, default='', max_length=500)
    phone = models.CharField(null=True, default='', max_length=500)
    text = models.CharField(null=True, default='', max_length=500)

    def __str__(self):
        return str(self.name)


class Product(TSFieldsIndexed):
    name = models.CharField(max_length=120, null=True, blank=True)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.name)
