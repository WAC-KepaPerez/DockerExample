from django.http import Http404, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
def hello_world(request):
    return render(request, 'hello_world.html', {})

class jsonMessage(APIView):
    def get(self, request, format=None):
        return Response({'succes': 'hello 667'}, status=status.HTTP_400_BAD_REQUEST)
    
class TodoDetail(APIView):
    def get(self, request):
        todomodels = Todo.objects.all()
        serializer = TodoSerializer(todomodels, many=True)
        return Response(serializer.data)
    

    def post(self, request):
            serializer = TodoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Todo = self.get_object(pk)
        Todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
