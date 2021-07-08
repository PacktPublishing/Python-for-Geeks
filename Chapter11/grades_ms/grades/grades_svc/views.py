from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Grade
from .serializers import GradeSerializer

class GradeViewSet(viewsets.ViewSet):

    def list(self, request):
        grades_list = Grade.objects.all()
        serializer = GradeSerializer(grades_list, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, id=None):
        myclass = Grade.objects.get(grade_id= id)
        serializer = GradeSerializer(myclass)
        return Response(serializer.data)