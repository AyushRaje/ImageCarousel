from django.contrib import admin
from main.models import Choice,Feedback
# Register your models here.
admin.site.register([
    Feedback,
    Choice,
])
    
    
