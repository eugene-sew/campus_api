

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Feedback
from .serializers import FeedbackSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method='get',
    responses={200: FeedbackSerializer(many=True)},
)
@swagger_auto_schema(
    method='post',
    request_body=FeedbackSerializer,
    responses={201: FeedbackSerializer, 400: 'Bad Request'},
)
@api_view(['GET', 'POST'])
def feedback_list_create(request):
    if request.method == 'GET':
        feedbacks = Feedback.objects.all()
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
