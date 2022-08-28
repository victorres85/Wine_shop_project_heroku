#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from celery import Celery
 # from __future__ import absolute_import
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wine_shop.settings')

app = Celery('wine_shop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(BROKER_URL=os.environ('REDIS_URL'),
                CELERY_RESULT_BACKEND=os.environ('REDIS_URL'))


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
