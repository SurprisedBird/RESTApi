from django.http import JsonResponse
from django.shortcuts import render

from firstApp.models import Employee


def employeeView(request):
    emp = {'id': 12, 'name': "Jhon", 'sal': 567}
    data = Employee.objects.all()

    response = {'employee': list(data.values('name', 'sal'))}
    a = JsonResponse(response)
    print(type(a))

    return JsonResponse(response)
