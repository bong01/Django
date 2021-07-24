from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Members
from .serializers import MembersSerializers
# Create your views here.


@csrf_exempt
def member_list(request):
    if request.method == 'GET':
        query_set = Members.objects.all()
        serializer = MembersSerializers(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MembersSerializers(data=data)
        # 클라이언트가 보낸 데이터가 Members 필드와 같으면
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        # 실패 시
        return JsonResponse(serializer.errors, status=400)