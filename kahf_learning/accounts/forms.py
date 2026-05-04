from django import forms
from .models import UserProfile

class CustomSignupForm(forms.Form):
    # first, last names are inbuilt in django user model
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder':'First Name'})
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder':'Last Name'})
    )

    phone = forms.CharField(
            max_length=15,
            required=False,
            widget=forms.TextInput(attrs={'placeholder':'Phone Number'})

        )

    # define allauth signup()
    def signup(self, request, user):
        """Called after user is created but before saved to handle additional fields"""
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        # save to db
        user.save()

        profile = UserProfile(user=user)
        profile.phone = self.cleaned_data.get('phone','')
        profile.save()
