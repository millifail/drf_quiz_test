from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serialzer import QuizSerialzer
import random

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("Hello world")


@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs= Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs),id)
    serialzer = QuizSerialzer(randomQuizs, many=True)
    return Response(serialzer.data)