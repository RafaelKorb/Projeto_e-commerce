from rest_framework import serializers

from .models import Whisky, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'whisky',
            'avaliador',
            'email',
            'avaliacao',
            'criacao',
            'ativo'
        )


class WhiskySerializer(serializers.ModelSerializer):

    class Meta:
        model = Whisky
        fields = (
            'nome',
            'type',
            'criacao',
            'ativo'
        )