from django.shortcuts import redirect
from django.urls import reverse
from allauth.mfa.utils import is_mfa_enabled

class MFARequiredMiddleware:
    """ middleware to enfore MFA at login """

    def __init__(self, get_response):
        self.get_response = get_response
        self.exempt_urls = [
            reverse('mfa_index'), # even the user is not signed mfa this page should be available that's why this is exempt_url
            reverse('mfa_activate_totp'),
            reverse('account_logout')
        ]
    
    def __call__(self, request):
        if request.user.is_authenticated:
            path = request.path_info
            print(path)

            is_exempt = any(path.startswith(url) for url in self.exempt_urls)

            if not is_exempt:
                if not is_mfa_enabled(request.user):
                    return redirect('mfa_index')

        
        # process the request normally
        response = self.get_response(request)
        return response