from rest_framework.serializers import ModelSerializer
from .models import Memo


class MemoSerializer(ModelSerializer):
    class Meta:
        model = Memo
        fields = [
            'title',
            'content',
            'author',
            'create_at',
            'id',
        ]
