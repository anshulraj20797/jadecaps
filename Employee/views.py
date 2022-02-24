from statistics import mode
from django.shortcuts import render
from rest_framework import viewsets
from Employee import models, serializers
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

class Employee50API(ListAPIView):
    queryset =  models.Employee.objects.filter(age__gt=50)
    serializer_class = serializers.EmployeeSerializer

class CompanyList(CreateAPIView, ListAPIView):
    queryset =  models.Company.objects.all()
    serializer_class = serializers.CompanySerializer

class CompanyDetails(RetrieveAPIView):
    queryset =  models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

    def retrieve(self, request, pk):
        queryset = models.Employee.objects.filter(company=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)