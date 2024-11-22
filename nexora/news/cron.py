from django_cron import CronJobBase, Schedule
from .views import update_news_data

class UpdateNewsJob(CronJobBase):
    RUN_EVERY_MINS = 60  # Run every hour

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'news.update_news_job' 

    def do(self):
        update_news_data()
