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
