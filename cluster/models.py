from django.conf import settings
from django.core.mail import send_mail
from django.db import models

class Registration(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    hackerrank_id = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    college_name = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    registered_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.hackerrank_id}"
    
    def approve_registration(self):
        """Method to approve registration and send notification email."""
        self.status = 'Approved'
        self.save()
        
        

    class Meta:
        permissions = [
            ("can_approve_registration", "Can approve contest registrations"),
        ]


class Contest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"