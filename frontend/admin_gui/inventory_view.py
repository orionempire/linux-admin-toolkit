from django.contrib import admin
from django.contrib.admin.sites import AdminSite

from django.contrib.auth.forms import *
from django.utils.translation import ugettext_lazy

from admin_gui.models import *


#create regular user (view). add CHANGE (only) permission for (physical list, virtual list)
class UserAdminAuthenticationForm(AuthenticationForm):
    """
    Same as Django's AdminAuthenticationForm but allows to login
    any user who is not staff.
    """    
    this_is_the_login_form = forms.BooleanField(widget=forms.HiddenInput,
                                initial=1,
                                error_messages={'required': ugettext_lazy(
                                "Please log in again, because your session has"
                                " expired.")})
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')        
        message = "ERROR Logging in."
         
        if username and password:
            self.user_cache = authenticate(username=username,
            password=password)
            if self.user_cache is None:
                if u'@' in username:
                    # Mistakenly entered e-mail address instead of username?
                    # Look it up.
                    try:
                        user = User.objects.get(email=username)
                    except (User.DoesNotExist, User.MultipleObjectsReturned):
                        # Nothing to do here, moving along.
                        pass
                    else:
                        if user.check_password(password):
                            message = _("Your e-mail address is not your "
                                        "username."
                                        " Try '%s' instead.") % user.username
                raise forms.ValidationError(message)
            # Removed check for is_staff here!
            elif not self.user_cache.is_active:
                raise forms.ValidationError(message)
        self.check_for_test_cookie()
        return self.cleaned_data
    pass

class UserAdmin(AdminSite):
    login_form = UserAdminAuthenticationForm
    
    # Anything we wish to add or override
    def has_permission(self, request):
        """
        Removed check for is_staff.
        """
        return request.user.is_active
 
user_admin_site = UserAdmin(name='inventory_view')

# View list of all physical servers and blades.    
class Physical_Machine_List_Admin(admin.ModelAdmin):
    list_display = ['physical_server_name','primary_ip_address','point_of_contact','role','purpose','host_enclosure_name']
    list_filter=['host_enclosure_name','role','purpose']    
    ordering = ['primary_ip_address']
    search_fields = ['host_enclosure_name','point_of_contact']        
    readonly_fields = ['physical_server_name','primary_ip_address','point_of_contact','role','purpose','host_enclosure_name']
    def has_add_permission(self, request):
        # Nobody is allowed to add
        return False
    def has_delete_permission(self, request, obj=None):
        # Nobody is allowed to delete
        return False
    
user_admin_site.register(Physical_Machine_List, Physical_Machine_List_Admin )

# View list of all physical servers and blades.           
class Virtual_Machine_List_Admin(admin.ModelAdmin):
    list_display = ['virtual_server_name','primary_ip_address','point_of_contact','role','purpose','host_server_name']
    list_filter=['host_server_name','role','purpose']    
    ordering = ['primary_ip_address']
    search_fields = ['host_server_name','point_of_contact']
    readonly_fields = ['virtual_server_name','primary_ip_address','point_of_contact','role','purpose','host_server_name']
    def has_add_permission(self, request):
        # Nobody is allowed to add
        return False
    def has_delete_permission(self, request, obj=None):
        # Nobody is allowed to delete
        return False
user_admin_site.register(Virtual_Machine_List, Virtual_Machine_List_Admin)
   