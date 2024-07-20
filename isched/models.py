from django.db import models

# Create your models here.

class JobSchedule(models.Model):
    job_id = models.CharField(max_length=255, unique=True, auto_created=True)
    job_name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.BooleanField(default=False)
    interval = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.job_name

class JobLog(models.Model):
    job_name = models.CharField(max_length=255)
    job_run_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_name,self.job_run_time.timestamp
