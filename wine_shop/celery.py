#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from celery import Celery
 # from __future__ import absolute_import
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wine_shop.settings')

app = Celery('wine_shop', broker='redis://:pcbbab5e12031f5fee7b14e4eae72e04d94cc5d4b72e880c9e6171313bc6b46bc@ec2-54-194-139-149.eu-west-1.compute.amazonaws.com:25540')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
