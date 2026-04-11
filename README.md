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