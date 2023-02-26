from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User
from django.http import JsonResponse
import face_recognition

from django.views.decorators.csrf import csrf_exempt
import json
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        #name = request.POST['name']
        #email = request.POST['email']
        #image_file = request.FILES['image']
        name = request.POST.get('name', '') # Use get method to get the value of 'name' key
        email = request.POST.get('email', '')
        image_file= request.FILES.get('image', None)
        image = face_recognition.load_image_file(image_file)
        face_encodings = face_recognition.face_encodings(image)[0]
        user = User(name=name, email=email,face_encodings=face_encodings)
        user.save()
        #return JsonResponse({'status': 'success'})
        messages.error(request, 'User registered')
        #return redirect('recognize')
        return render(request, 'register.html')
    #else:
        #return JsonResponse({'status': 'error'})
        #return redirect('register')
    return render(request, 'register.html')
    
    
def recognize(request):
    if request.method == 'POST':
        image_file = request.FILES['image']
        image = face_recognition.load_image_file(image_file)
        face_encodings = face_recognition.face_encodings(image)
        recognized_users = []
        for face_encoding in face_encodings:
            users = User.objects.all()
            for user in users:
                user_face_encoding = face_recognition.face_encodings(user.face_encodings)[0]
                distance = face_recognition.face_distance([user_face_encoding], face_encoding)[0]
                if distance < 0.6:
                    recognized_users.append({'name': user.name, 'email': user.email})
                    return JsonResponse({'status': 'success', 'recognized_users': recognized_users})
                else:
                    return JsonResponse({'status': 'error'})
        
    return render(request, 'recognize.html')


def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('users')

def update_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        image = request.FILES['image']
        user.name = name
        user.email = email
        user.image = image
        user.save()
        return redirect('users')
    return render(request, 'update_user.html', {'user': user})

