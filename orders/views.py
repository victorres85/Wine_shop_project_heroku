from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.http import HttpResponse
from cart.cart import Cart
import weasyprint
from .forms import OrderCreateForm
from .models import Order, OrderItem
from django.core.mail import send_mail

#from ..filesremoved.tasks import order_created
from django.conf import settings

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


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         wine=item['wine'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task

            order_created(order.id)
            #set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('payment:process'))

    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {
        'cart': cart,
        'form': form
    })


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})

@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(
        response,
        stylesheets=[weasyprint.CSS(settings.STATIC_ROOT / 'css/pdf.css')])
    return response
