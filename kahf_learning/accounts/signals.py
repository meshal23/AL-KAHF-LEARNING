from allauth.account.signals import email_confirmed
from django.dispatch import receiver #this decorator connect recievers to signals
from django.utils import timezone

@receiver(email_confirmed)
def email_confirmed_handler(request, email_address, **kwargs): #when this email_confirmed signal trigger this function will be execute
    user = email_address.user

    user.profile.email_verified_at = timezone.now()
    user.profile.save()

    
    