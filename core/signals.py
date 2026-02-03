import time
import threading
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product

@receiver(post_save, sender=Product)
def product_signal(sender, instance, **kwargs):

    # Question 1: Synchronous prove
    print("Signal START")
    time.sleep(5)
    print("Signal END")

    # Question 2: Same thread prove
    print("Signal Thread ID:", threading.get_ident())

    # Question 3: Same transaction prove
    print(
        "Visible inside transaction:",
        Product.objects.filter(id=instance.id).exists()
    )
