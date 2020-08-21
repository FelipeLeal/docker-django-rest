from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import chile_rut

def validate_rut(value):
    """
    Check if value is a valid Chilean RUT ("rol único tributario")
    :param value:
    :return:
    """
    if chile_rut.validate_rut(value):
        raise ValidationError(
            _('%(value) is not a valid RUT'),
            params={'value': value},
        )

def validate_dose(value):
    if not 0.15 <= float(value) <= 1.0 :
        raise ValidationError(
            _('dose: %(value) must be between 0.15 and 1.0'),
            params={'value', value}
        )