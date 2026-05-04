# Django Unfold
- uv add django-unfold
- INSTALLED_APPS add "unfold" at top
- admin.py import ModelAdmin (see in admin.py)
- from now on every model register by ModelAdmin

# django-import-export
- it is a package that easily import and export csv, json files to the database
- add import-export in INSTALLED_APPS

# sorting imports in most pythonic way
- uv add isort
- then in the terminal, isort ./accounts/admin.py
- this will sort all your imports in admin.py in most pythonic way
=======
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

## 5. customizing django allauth - custom signup forms and logic

- how to add extra fields for the signup page
  - models.py create UserProfile model (see in models.py) - this is how you override the default User model that given by django then you can add the custom fields for UserProfile model
  - the you makemigrations, migrate
- add the custom fields in allauth signup form
  - https://docs.allauth.org/en/latest/account/configuration.html , here go to Signup section , there you can see ACCOUNT_SIGNUP_FORM_CLASS
  - create forms.py and create CustomSignupForm class (see in forms.py)
  - now go to settings.py and add ACCOUNT_SIGNUP_FORM_CLASS (see in forms.py)
  - now add the user to UserProfile table with phone_no field that is not in the default django user table, for that in forms.py we set the signup() after we save the user into the db (see in forms.py -> CustomSignupForm class)

## 6. views, templates customizations

- go to https://docs.allauth.org/en/latest/account/views.html , it's very easy to extend these views and create our own class based views inherit from these and point to url of our custom class
- #### 1. override the default allauth signup view
  - in the views.py import messages(django.contrib), SignupView(allauth.account.views), app_settings(allauth.account) [see views.py]
  - create CustomSignupView class (see views.py) and override the form_valid method given from allauth SignupView class (see in views.py)
  - and for tell django to use this custom signup view go to main urls.py and add our CustomSignupView as same url of the allauth signup path
  - go to the template (the template the signup will redirect) and show the messages (secret.html)
- #### 2. adding custom context data ti SignupView
  - like before we override the built in get_context_data() method and add custom attractive message to get users to signup (see views.py)
  - to display that message in the docs https://docs.allauth.org/en/latest/common/templates.html , now we're going to override the built in template
  - go to https://codeberg.org/allauth/django-allauth/src/branch/main/allauth/templates , then copy the signup.html
  - create templates --> accounts --> signup.html and paste the code , the path is very important, now you can modify the template from here
  - now you can add your custom message in your signup template (see in accounts/signup.html)
  - developer copy all templates and style when they want

## 7. allauth signals

- when user register or confirm email address etc, wire up a signal to react for those events
- https://docs.allauth.org/en/latest/account/signals.html
- create signals.py inside our project
- add custom email_confirmed_handler() to excute when email_confirmed signal trigger (see signals.py)
- run the server and signup , an email verification lik will be sent, before you confirm the email, first we import our signals to apps.py in built in ready() method (see in apps.py)
- so in our UserProfile table there is a column email_verifed_at we're going to fill with this signal (see signal.py)

## 8. social authentication

- https://docs.allauth.org/en/latest/socialaccount/introduction.html
- uv add "django-allauth[socialaccount]"
- in the INSTALLED_APPS add 'allauth.socialaccount', 'allauth.socialaccount.providers.google'
- then you should register the application (google cloud)
- uv run manage.py migrate (tables socialaccount, socialapp, socialtoken will be created)
- socialtoken stores oAuth token for each social account
- create a social account with admin panel
- before that https://docs.allauth.org/en/latest/socialaccount/providers/google.html , you should register in google cloud
- get oAuth credentials
  - create a project in google cloud
  - see the workflow in AL KAHF LEARNING RESOURCES folder/ set up google social signup
- access social account's data
  - go to https://docs.allauth.org/en/latest/socialaccount/templates.html
  - go to secret.html and analyze the docs template tags to see how it's implemented
  - another template tag implemented in index.html
  - let's say another scenario, a user has an account johndoe@gmail.com and you created that account using username, password after you trying to signin with your google account with this same email address, what should happen
    - SOCIALACCOUNT_EMAIL_AUTHENTICATION, this is when social email address already taken by the local user by default it is False if you go to setting.py and adjust SOCIALACCOUNT_PROVIDERS, set 'EMAIL_AUTHENTICATION': True,
      and then only SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = True,
      if you set this the social account automatically connect with local account
    - this only possible if your email is verified

## 9. with multiple providers (github)

- https://docs.allauth.org/en/latest/socialaccount/providers/github.html
- register your application here https://github.com/settings/applications/new
- you add http://127.0.0.1:8000/accounts/github/login/callback/ exactly as callback url
- register your app
- in settings.py add github in INSTALLED_APPS
- in settings.py configure github in SOCIALACCOUNT_PROVIDERS
- django admin add github in social_applications table
- that's it
- how can i add social accounts for existing users
  - just go to the allauth signin page and signup then click email --> Account settings add your new github there
- adding github profile
  - secret.html

## 10. Multi factor authentication (MFA)

- https://docs.allauth.org/en/latest/mfa/introduction.html
- mfa, enhace security, protect against phishing, identity verification
- uv add "django-allauth[mfa]"
- add "allauth.mfa" in INSTALLED_APPS in settings.py --> uv run manage.py migrate
- this will create mfa_authenticator table in the db
- you also set mfa pattern in the main urls.py (see main urls.py)
- Now we're going to configure our app to mfa https://docs.allauth.org/en/latest/mfa/configuration.html
- now we can add 2 factor authentication after we sign in , then set up with authenticator with qrcode then we all setup
- take a look at mfa_authenticator table , the user will connected to two factor authentication
- #### usage of recovery codes
  - let's say you lost your phone so your authenticator app gone, but you still want to access the web app how to dothis
  - you just add one of the recovery codes you have downloaded rather than add the code thaat authenticator gives to you
- #### adding middleware
  - reason is if we decide all users must set mfa to use this webapp
  - when a user sign in, when the user not have authenticator installed we redirect to this two factor authentication page
  - create middleware.py inside you app (accounts) (see middleware.py)
  - add this middleware in settings.py
  - very important you should add below "django.contrib.auth.middlewareAuthenticationMiddleware" because middleware are executing one by one and we should add this middleware after user is authenticated

## 11. all-auth-ui

- provides nice looking ui for django allauth
- https://github.com/danihodovic/django-allauth-ui
- uv add django-allauth-ui
- in settings.py
  - add allauth_ui in INSTALLED_APPS, before django_allauth
  - then also add widget_tweaks, slipper at the bottom
- this will create nice looking forms in allauth pages (under hood tailwind + daisyui)
- add daisyui themes (dark, light, cupcake)
  - settings.py add ALLAUTH_UI_THEME = 'cupcake'
- internationalisation using multiple languages
  - in settings.py LANGUAGE_CODE = 'fr' will set your sign up page in french
