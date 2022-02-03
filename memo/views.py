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


@api_view(['GET','POST'])
def memo_list(request,nickname):
    if request.method=='GET':
        memo = Memo.objects.filter(author=nickname)
        serializer = MemoSerializer(memo, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    elif request.method=='POST':
        memo = MemoSerializer(data=request.data)
        if memo.is_valid():

            memo.save()
            return Response(status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def memo_detail(request,pk,nickname):
    try:
        memo = Memo.objects.get(id=pk)
    except Memo.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = MemoSerializer(memo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = MemoSerializer(memo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        memo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@login_required(login_url='/accounts/login')
def index(request):
    try :
        Profile.objects.get(user_id = request.user.pk)

        return render(request, 'memo/index.html')
    except Profile.DoesNotExist :
        return redirect('accounts:create_nickname')

