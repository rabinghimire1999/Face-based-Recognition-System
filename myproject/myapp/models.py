from django.db import models
import json
from django.core.validators import FileExtensionValidator

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    #image = models.ImageField(upload_to='images/', validators=[
    #    FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
     #     # 5 MB in bytes
    #])
    face_encodings = models.TextField(null=True, default=None)

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'image':self.image,
        }

    @staticmethod
    def deserialize(data):
        return User(
            name=data['name'],
            email=data['email'],
            image=data['image'],
        )
