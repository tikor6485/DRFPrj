from django.db.models.query import QuerySet
from rest_framework import serializers, viewsets
from .models import Person
from .serializers import PersonSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class PersonViewset(viewsets.ModelViewSet):

    queryset = Person.objects.all()
    serializer_class=PersonSerializer



    # def list(self, request):
    #     querySet = Person.objects.all()
    #     serializer = PersonSerializer(querySet, many = True)
    #     return Response (serializer.data)

    # def create(self, request):
    #     serializer = PersonSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'message':'OK'})
    #     else:
    #         return Response(serializer.errors)

    # def retrieve(self, request, pk=None):
    #     querySet = Person.objects.all()
    #     person = get_object_or_404(querySet, pk=pk)
    #     serializer = PersonSerializer(person)
    #     return Response(serializer.data)



    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass