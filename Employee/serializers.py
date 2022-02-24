from dataclasses import fields
from pyexpat import model
from statistics import mode
from rest_framework import serializers
from Employee import models


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ['id', 'name']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ['id', 'name', 'age', 'company']

    def to_representation(self, instance):
        emp = super(EmployeeSerializer, self).to_representation(instance)
        emp['company'] = instance.company.name
        return emp
