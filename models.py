from django.db import models

#For the PainRecord in the dashboard
class PainRecord(models.Model):
    pain_type = models.CharField(max_length=100)
    severity = models.IntegerField()
    duration = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    trigger = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pain_type} - {self.severity}/10"
    
    
    
    
