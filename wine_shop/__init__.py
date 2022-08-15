#!/usr/bin/env python
# -*- coding: utf-8 -*-

import celery
from .celery import app as celery_app

__all__ = ['celery_app']
