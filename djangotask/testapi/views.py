from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotAllowed
from django.core.exceptions import ObjectDoesNotExist
from .models import Users

@csrf_exempt

def createUser(request):
    data=json.load(request)
    try:
        user=Users.objects.create(name=data['name'],email=data['email'],gender=data['gender'],password=data['password'])
        
        response = {
        "message": "User created successfully",
        }

        return HttpResponse( json.dumps(response),  status=200)
    except Exception as e:
        response = {
        "error": str(e),
        }
        return HttpResponse( json.dumps(response),  status=400)
    
@csrf_exempt

def getUser(request):
    data=json.load(request)
    
    try:
        user=Users.objects.get(email=data['email'])
        response = {
        "name": user.name,
        "email": user.email,
        "gender": user.gender,
        "password": user.password
        }
        return HttpResponse( json.dumps(response),  status=200)
    except Exception as e:
        response = {
        "error": str(e),
        }
        return HttpResponse( json.dumps(response),  status=400)
    
@csrf_exempt
   
def deleteUser(request):
    data=json.load(request)
    try:
        user=Users.objects.get(email=data['email'])
        user.delete()
        response = {
        "message": "User deleted successfully",
        }
        return HttpResponse( json.dumps(response),  status=200)
    except Exception as e:
        response = {
        "error": str(e),
        }
        return HttpResponse( json.dumps(response),  status=400)
    
@csrf_exempt

def updateUser(request):
    data=json.load(request)
    try:
        user=Users.objects.get(email=data['email'])
        updateData=data["updateData"]
        
        if 'name' in updateData:
            user.name=updateData['name']
        if 'email' in updateData:
            user.email=updateData['email']
        if 'gender' in updateData:
            user.gender=updateData['gender']
        if 'password' in updateData:
            user.password=updateData['password']
        user.save()
        response = {
        "message": "User updated successfully",
        }
        return HttpResponse( json.dumps(response),  status=200)
    except Exception as e:
        response = {
        "error": str(e),
        }
        return HttpResponse( json.dumps(response),  status=400)
            
        
        
        

