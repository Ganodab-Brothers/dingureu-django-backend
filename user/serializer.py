import typing, re
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_text
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from user.models import User, School


def validate_username(username):
    rule = re.compile("[a-zA-Z0-9._]*$")  # alphanumeric and underscore
    if not rule.match(username):
        raise serializers.ValidationError(
            'Username must be alphanumeric, dot and underscore(_).')


def validate_phone_number(value):
    error_message = 'This field must be following format: "+821012341234".'
    if value[0] != "+":
        raise serializers.ValidationError(error_message)
    filtered = value[1:]  # remove the '+' at the front
    if not filtered.isnumeric():  # the rest of value should be numeric
        raise serializers.ValidationError(error_message)


def validate_numeric(value):
    if not value.isnumeric():
        raise serializers.ValidationError('This field must be numeric.')


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        min_length=5,
        validators=[
            UniqueValidator(queryset=User.objects.all()),
            validate_username,
        ],
        max_length=30,
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[
            validate_password,
        ],
        min_length=1,
        max_length=128,
    )
    birthday = serializers.DateField(required=False)
    phone_number = serializers.CharField(
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all()),
            validate_phone_number,
        ],
        max_length=14)
    school_code = serializers.CharField(
        required=True,
        write_only=True,
        validators=[
            validate_numeric,
        ],
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