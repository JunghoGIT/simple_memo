from django.test import TestCase
from .serializers import MemoSerializer


data = {
    'content' : '내용',
    'title' : '제목',
    'author' : '관리자'
}

memo = MemoSerializer(data=data)
print(memo)

print(memo.is_valid())
