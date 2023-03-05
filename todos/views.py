from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Todo
from .serializers import TodoCreateSerializer

@api_view(['POST'])
def todo_create(request):
    serializer = TodoCreateSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(data={'detail': 'Please enter correct detail'}, status=status.HTTP_400_BAD_REQUEST)
    
    todo = Todo()

    todo.name = serializer.validated_data.get('name')
    todo.is_complete = serializer.validated_data.get('is_complete')
    todo.description = serializer.validated_data.get('description', None)

    todo.save()
    return Response()


@api_view(['GET'])
def todo_list(request):
    todos = Todo.objects.all()
    data = []
    for t in todos:
        data.append({ 'id': t.id, 'name': t.name, 'is_complete': t.is_complete })
    return Response(data=data)

@api_view(['GET'])
def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    return Response(data={'id': todo.id, 'name': todo.name, 'is_complete': todo.is_complete, 'description': todo.description, 'created_at': todo.created_at})