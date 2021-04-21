import typing
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_text
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from user.models import User, School


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all()),
        ],
        max_length=30,
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        min_length=1,
        max_length=128,
    )
    birthday = serializers.DateField(required=False)
    phone_number = serializers.CharField(
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all()),
        ],
        max_length=14)
    school_code = serializers.CharField(
        required=True,
        write_only=True,
        max_length=20,
    )
    school_name = serializers.CharField(
        required=True,
        write_only=True,
        max_length=30,
    )
    school = serializers.SlugRelatedField(
        slug_field='school_name',
        read_only=True,
    )

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'nickname',
            'phone_number',
            'gender',
            'birthday',
            'student_id',
            'school_code',
            'school_name',
            'school',
        )

    def create(_, data: typing.Dict):
        school: School = School.objects.get_or_create(
            school_code=data['school_code'],
            school_name=data['school_name'],
        )[0]
        user = User.objects.create(
            username=data['username'],
            password=data['username'],
            nickname=data['nickname'],
            phone_number=data['phone_number'],
            birthday=data['birthday'],
            student_id=data['student_id'],
            school=school,
        )
        user.set_password(data['password'])
        user.save()
        return user


class UserSerializerDocument(UserSerializer):
    password = None

    class Meta(UserSerializer.Meta):
        fields = (
            'username',
            'nickname',
            'phone_number',
            'gender',
            'birthday',
            'student_id',
            'school_code',
            'school_name',
            'school',
        )