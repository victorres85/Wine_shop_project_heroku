#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from celery import Celery
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wine_shop.settings')
app = Celery('wine_shop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
