#Question 1
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone

#Question 2
from .models import Article
import threading

#Question 3
from .models import Order, OrderLog


#Question 1
# Signal handler that simulates a time-consuming task
@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, created, **kwargs):
    if created:
        print(f"Signal received for User: {instance.username} at {timezone.now()}")
        time.sleep(5)  # Simulating a delay
        print("Signal handler execution finished at:", timezone.now())




#Question 2
# Signal handler that is executed after an Article is saved
@receiver(post_save, sender=Article)
def article_saved(sender, instance, created, **kwargs):
    if created:
        # Printing the thread ID in the signal handler
        print(f"Signal Handler Thread ID: {threading.get_ident()}")




#Question 3
# Signal handler to create a log entry when an order is created
@receiver(post_save, sender=Order)
def log_order_creation(sender, instance, created, **kwargs):
    if created:
        # Logging the creation of the order in the OrderLog
        OrderLog.objects.create(order=instance, message=f"Order for {instance.item} created.")

