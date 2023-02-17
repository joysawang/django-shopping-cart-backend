from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

class AdminAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)