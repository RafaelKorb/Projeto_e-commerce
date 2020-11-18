from rest_framework import generics
from rest_framework.generics import get_object_or_404


from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
#from rest_framework import mixins

#from rest_framework import permissions


from .models import Whisky, Avaliacao
from .serializers import WhiskySerializer, AvaliacaoSerializer
#from .permissions import EhSuperUser


class WhiskysAPIView(generics.ListCreateAPIView):
    queryset = Whisky.objects.all()
    serializer_class = WhiskySerializer


class WhiskyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Whisky.objects.all()
    serializer_class = WhiskySerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('whisky_pk'):
            return self.queryset.filter(whisky_id=self.kwargs.get('whisky_pk'))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    
    def get_object(self):
        if self.kwargs.get('whisky_pk'):
            return get_object_or_404(self.get_queryset(), whisky_id=self.kwargs.get('whisky_pk'), pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


####v2####

class WhiskyViewSet(viewsets.ModelViewSet):
#    permission_classes = (
#        EhSuperUser,
#        permissions.DjangoModelPermissions,
#    )
    queryset = Whisky.objects.all()
    serializer_class = WhiskySerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
#       self.pagination_class.page_size=2
        whisky = self.get_object()
        #avaliacoes = Avaliacao.objects.filter(curso_id=pk)
#        page = self.paginate_queryset(avaliacoes)

#        if page is not None:
#            serializer = AvaliacaoSerializer(page, many=True)
#            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(whisky.avaliacoes.all(), many=True)
        return Response(serializer.data)


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer