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
