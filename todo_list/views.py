from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import todoSerializer
from .models import todo

# Create your views here.
@api_view(["GET"])
def todolist(req):
    todo_list = todo.objects.all()
    serializer = todoSerializer(todo_list, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def todocreate(req):
    serializer = todoSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(["DELETE"])
def tododelete(req, pk):
    to_do = todo.objects.get(id=pk)
    to_do.delete()
    return Response("Delete Success")


@api_view(["PUT"])
def todoupdate(req, pk):
    to_do = todo.objects.get(id=pk)
    serializer = todoSerializer(to_do, data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)