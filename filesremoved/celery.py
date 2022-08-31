#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import absolute_import, unicode_literals
import os
from django.conf import settings
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wine_shop.settings')

app = Celery('wine_shop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()




@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
