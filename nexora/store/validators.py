import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 8:
            raise ValidationError(
                _("password must be at least 8 characters long."),
                code='8_character_long',
            )
        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                _("password must contain at least one uppercase letter."),
                code='password_no_upper',
            )
        if not re.search(r'[a-z]', password):
            raise ValidationError(
                _("password must contain at least one lowercase letter."),
                code='password_no_lower',
            )
        if not re.search(r'[0-9]', password):
            raise ValidationError(
                _("password must contain at least one number."),
                code='password_no_number',
            )
        if not re.search(r'[\w_]', password):
            raise ValidationError(
                _("password must contain at least one special character (e.g., !, @, #, $, %, ^, &, ?, *)."),
                code='password_no_special',
            )
    def get_help_text(self):
        return _(
            "Your password must contain at least one uppercase letter, one lowercase letter, one number,"
            "and one special character."
        )