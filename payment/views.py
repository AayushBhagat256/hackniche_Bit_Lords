from django.shortcuts import render
import razorpay
from hacknicheproject.settings import RAZORPAY_API_SECRET_KEY, RAZORPAY_API_KEY

# Create your views here.
client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def pay(request):

    if request.POST==True:
        razorpay_payment_id = request.razorpay_payment_id
        razorpay_order_id  = request.razorpay_order_id
        razorpay_signature = request.razorpay_signature

        bool = client.utility.verify_payment_signature({
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
        })

    amount = 10000
    amount_disp = 100
    DATA = {
        "amount": amount,
        "currency": "INR",
    }
    pay_order = client.order.create(data=DATA)
    pay_order_id = pay_order['id']

    context = {
        'amount': amount,
        'api_key': RAZORPAY_API_KEY,
        'order_id': pay_order_id,
        'amount_disp' : amount_disp,
    }
    return render(request,'payment.html',context)