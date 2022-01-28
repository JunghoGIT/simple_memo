from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import MemoSerializer
from rest_framework.response import Response
from .models import Memo
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def memo_list(request):
    if request.method=='GET':
        memo = Memo.objects.all()
        serializer = MemoSerializer(memo, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
