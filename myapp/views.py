#Question 1
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils import timezone

#Question 2
from .models import Article
import threading

#Question 3
from django.db import transaction
from .models import Order, OrderLog



def home(request):
    return HttpResponse("Welcome to the Home Page!")



#Question 1
#function where a User instance is created
def register_user(request):
    print("Creating user at:", timezone.now())
    user = User.objects.create(username='testuser4')
    print("User created at:", timezone.now())
    return HttpResponse("User created")




#Question 2
def create_article(request):
    # Printing the thread ID in the main function before creating the article
    print(f"Caller Thread ID: {threading.get_ident()}")

    # Creating a new Article instance, which will trigger the signal
    Article.objects.create(title='Test Article', content='This is a test article.')

    return HttpResponse("Article created")



#Question 3
def create_order_with_rollback(request):
    order = None  
    try:
        with transaction.atomic():
            # Creating an order, which will trigger the post_save signal
            order = Order.objects.create(item='Laptop', quantity=1)

            
            if OrderLog.objects.filter(order=order).exists():
                print("OrderLog entry created.")

            # Forcefully raising an exception to rollback the transaction
            raise Exception("Forcing a rollback")
    except Exception as e:
        print(f"Exception occurred: {e}")

    # Checking if the OrderLog entry still exists after the rollback
    if order is not None and OrderLog.objects.filter(order=order).exists():
        print("OrderLog entry exists after rollback. Signal runs outside transaction.")
    else:
        print("OrderLog entry does not exist after rollback. Signal runs inside transaction.")

    return HttpResponse("Orders")






