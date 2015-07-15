from django.shortcuts import render, redirect
from django.core import serializers
import json
from django.http import HttpResponse, JsonResponse
from repositories.device_repository import DeviceRepository
from repositories.user_repository import UserRepository

# Create your views here.

def index(request):
    dr = DeviceRepository()
    devices = dr.get_all_devices()
    free_devices = list(filter((lambda x: x.reserved_by is None), devices))

    return render(request, 'www/index.html', {
        'devices': devices,
        'free_devices': free_devices
    })

def reserve(request):
    device_pk = request.GET.get('device_pk', '')
    user_pk = request.GET.get('user_pk', '')

    dr = DeviceRepository()
    ur = UserRepository()

    device = dr.get_by_pk(device_pk)
    user = ur.get_by_pk(user_pk)

    device.reserve(user)

    return redirect('devices:index')

def free(request, pk):
    dr = DeviceRepository()
    device = dr.get_by_pk(pk)
    device.set_free()

    return redirect('devices:index')

def users(request):
    last_name = request.GET.get('last_name', '')
    ur = UserRepository()

    users = ur.get_by_last_name(last_name)

    json_users = json.loads(serializers.serialize('json', users))

    response = {'suggestions': []}

    for user in json_users:
        response['suggestions'].append({
            'value': ' '.join([user['fields']['first_name'], user['fields']['last_name']]),
            'data': user['pk']
        })

    return JsonResponse(response, safe=False)
