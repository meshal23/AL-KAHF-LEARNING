from django.contrib import admin

# ---- django unfold user admin styling start ---- #
# django unfold's normal ModalAdmin cannot adopt the default django user model that's 
# why this setup

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin

# django-import-export configuration
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

# ---- django unfold user admin styling end ---- #


#---- add import export for a particular modal example ---- #

    # class ExampleModal(ModelAdmin, ImportExportModelAdmin):
    #     import_form_class = ImportForm
    #     export_form_class = ExportForm
    #     # export_form_class = SelectableFieldsExportForm

        # for filtering
        # list_filter = ['col1']

        # finally you should have submit button for actual filtering
        # list_filter_submit = True

        # there are lot of filters to add for a modal
        # https://unfoldadmin.com/docs/filters/introduction/



