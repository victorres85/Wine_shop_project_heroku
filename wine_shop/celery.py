#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from celery import Celery
from decouple import config


#from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wine_shop.settings')

app = Celery('wine_shop', broker='redis://redis:8000/0')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
