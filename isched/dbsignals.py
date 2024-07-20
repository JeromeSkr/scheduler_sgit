from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Job_schedule
from isched.views import scheduler3
from django.db.models.signals import post_migrate
from isched.scheduler import schedule_jobs_check_db
from apscheduler.schedulers.background import BackgroundScheduler


@receiver(post_migrate)
@receiver(post_save, sender=Job_schedule)
@receiver(post_delete, sender=Job_schedule)
def job_schedule_altered(sender, instance, **kwargs):
    # Your function to run when a Job_schedule is saved
    # schedule_1.shutdown()
    # schedule_1 = schedule_2 = BackgroundScheduler()
    # scheduler3()

    schedule_jobs_check_db()