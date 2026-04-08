from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# for override the default allauth views
from django.contrib import messages
from allauth.account.views import SignupView
from allauth.account import app_settings

# custom sign up view
class CustomSignupView(SignupView):
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['custom_message'] = "Gain knowledge, rule the right way—learn smarter, faster, and on your terms. 🚀"
        return context
    
    def form_valid(self, form):
        # here you can add custom logic before saving
        response =  super().form_valid(form) #this allauth SignupView class has form_valid function we are overriding it

        # we are showing some flash messages
        if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY: #we set optional in out EMAIL_VERIFICATION on settings.py
            messages.info(
                self.request,
                "We've sent you an email to verify your account. please check your inbox."
            )
        else:
            messages.success(
                self.request,
                f"Welcome {form.cleaned_data['first_name']}! Your account has been created"
            )
        return response

def index(request):
    return render(request, 'index.html')

@login_required
def secret(request):
    return render(request, 'secret.html')

