from mezzanine.twitter.models import Query
from celery.decorators import periodic_task
from datetime import timedelta

@periodic_task(run_every=timedelta(minutes=10))
def poll_twitter():
    for query in Query.objects.filter(interested=True):
        query.run()
