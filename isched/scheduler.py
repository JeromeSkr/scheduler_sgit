from django.utils import timezone
from datetime import datetime as d
from .models import JobSchedule, JobLog
import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

def run_scheduled_jobs():
    current_time = d.now()
    jobs = JobSchedule.objects.filter(start_time__lte=current_time, end_time__gte=current_time, status=True)
    
    for job in jobs:
            # Calculate if the job should run at the current time based on the interval
            # time_since_start = (current_time - job.start_time).total_seconds()
            # if int(time_since_start / 60) % job.repeat_interval == 0:
                JobLog.objects.create(job_name=job.job_name)
                print(f"{job.job_name} executed at {current_time}")


def schedule_jobs_check_db():
    print(f"Checked db at {d.now()}")
    run_scheduled_jobs()

