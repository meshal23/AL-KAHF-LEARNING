# Django All-Auth Integration

- https://docs.allauth.org/en/latest/installation/quickstart.html

## 1. install django-allauth

- uv add django-allauth
- settings.py add AUTHENTICATION_BACKENDS (in the docs)
- add somethings to INSTALLED_APPS (in the docs)
- add middleware in settings.py (see in docs)
- add all auth url config in project's main urls.py
- uv run python manage.py migrate
- ### -- that's it we set up all auth--

- #### Observation
  - we can see in our database 2 new tables will created (account_emailaddress, account_emailconfirmation)
  - this will allow user can have multiple email address and use 1 email as primary
  - django default allows only one email per user but all auth gives the privilage to have many

## 2. deep dive authentication, registration, more

- allauth distinct between
  - regular accounts
  - social accounts
- account system gives you complete customizable authentication system so you can do (sign in, sign up, logout, password management, email verification, also social login, also templates integration, rate limits )
- we already installed in INSTALLED_APPS ('allauth_account')
- in the url if you go any @login_required decorated url it redirect you to the allauth page
- if you go signup and then first it gives you connectionRefusedError
  #### why
  - because allauth try to send verification for your email address so if you have wrong email this error will show
  - to resolve you go to https://docs.allauth.org/en/latest/account/configuration.html. here go to Email Verification -> ACCOUNT_EMAIL_VERIFICATION='optional', we make this 'none' in settings.py
  - make sure you add 'django.contrib.sites' in INSTALLED_APPS, 'SITE_ID=1' s(see in settings.py)
- verify user with email
    - for that we ACCOUNT_EMAIL_VERIFICATION='optional'
    - but for prevent the connectionRefusedError
    - we add EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        - this will give the verification on the terminal (very good for development & tesing)
        - if we click the email link and confirm, and check in the accounts_emailaddress table verfied turns to 1
    - #### adding multiple email addresses for one user
        - go to http://127.0.0.1:8000/accounts/email/ and add the email, check accounts_emailaddress table

## 3.customizing the registration form
- https://docs.allauth.org/en/latest/account/configuration.html here go to SignUp section
- there ACCOUNT_SIGNUP_FIELDS we define in settings.py as ['email', 'password1','password2'] (see settings.py)
- ACCOUNT_LOGIN_METHODS = {'email', 'username'} this will ask you can either add username or email
- ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = True
for this you should set ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
this will only show email field for signup, if you add your email this will send a code for your email, then you paste that code here
- this method of authentication now available for login also

## 4.django-allauth views and forms
- go to https://docs.allauth.org/en/latest/account/views.html ,
- these are customizable by extending these classes
- https://docs.allauth.org/en/latest/account/forms.html , you can extend these forms and you can customize by your needs
- https://docs.allauth.org/en/latest/account/decorators.html ,
    - for example there is verified_email_required decorator you add on a view so that view function will only accessed by email verification
- there is also something called ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE , log a user out when password change happens you set this on settings.py
- also there is signals emitting througout the authentication process https://docs.allauth.org/en/latest/account/signals.html you can notify or something with it
- Rate Limits
    - https://docs.allauth.org/en/latest/account/rate_limits.html
    - we can access through ACCOUNT_RATE_LIMITS setting
    - we can set many limits for example "change_password" (default: "5/m/user") means per user only 5 times to request change password api for a minute
