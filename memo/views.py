from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .serializers import MemoSerializer
from rest_framework.response import Response
from .models import Memo
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from accounts.models import Profile

# Create your views here.


@api_view(['GET'])
def memo_list(request):
    if request.method=='GET':
        memo = Memo.objects.all()
        serializer = MemoSerializer(memo, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@login_required(login_url='/accounts/login')
def index(request):
    try :
        Profile.objects.get(user_id = request.user.pk)

        return render(request, 'memo/index.html')
    except Profile.DoesNotExist :
        return redirect('accounts:create_nickname')

