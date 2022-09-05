#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.mail import send_mail

from celery import shared_task
from ..orders.models import Order

import celery
app = celery.Celery('example')


@shared_task
def order_created(order_id):
    """
   Task to send an e-mail notification when an order is
   successfully created.  
   """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject, message, 'admin@wine_shop.com',
                          [order.email])
    return mail_sent
