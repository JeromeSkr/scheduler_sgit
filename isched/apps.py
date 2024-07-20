from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from isched.scheduler import schedule_jobs_check_db


class IschedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'isched'

    def ready(self):
        bg_scheduler = BackgroundScheduler()
        bg_scheduler.add_job(schedule_jobs_check_db, IntervalTrigger(seconds=10))
        bg_scheduler.start()

        # Shut down the scheduler when exiting the app
        import atexit
        atexit.register(lambda: bg_scheduler.shutdown())