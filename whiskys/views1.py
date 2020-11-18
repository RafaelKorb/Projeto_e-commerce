from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Whisky, Avaliacao
from .serializers import WhiskySerializer, AvaliacaoSerializer


class WhiskyAPIView(APIView):

    def get(self, request):
        whiskys = Whisky.objects.all()
        serializer = WhiskySerializer(whiskys, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WhiskySerializer(data=request.data)
        serializer.is_valid(raised_execption=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raised_execption=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
