import boto3, logging
from botocore.exceptions import ClientError
from django.http.request import HttpRequest
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from config import envs
from file import serializers
from file.serializers import FileSerializer


def create_presigned_post(bucket_name,
                          object_name,
                          fields=None,
                          conditions=None,
                          expiration=3600):
    """Generate a presigned URL S3 POST request to upload a file

    :param bucket_name: string
    :param object_name: string
    :param fields: Dictionary of prefilled form fields
    :param conditions: List of conditions to include in the policy
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Dictionary with the following keys:
        url: URL to post to
        fields: Dictionary of form fields and values to submit with the POST
    :return: None if error.
    """

    # Generate a presigned S3 POST URL
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_post(bucket_name,
                                                     object_name,
                                                     Fields=fields,
                                                     Conditions=conditions,
                                                     ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL and required fields
    return response


class FileView(viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = FileSerializer

    @action(detail=False, methods=["PUT"])
    def upload(self, request: HttpRequest):
        object_name = request.data['object_name']
        s3_data = create_presigned_post(envs.BUCKET_NAME, object_name)
        serializers: FileSerializer = self.get_serializer(s3_data)
        return Response(serializers.data)
