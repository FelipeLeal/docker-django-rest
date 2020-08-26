from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import chile_rut


def validate_rut(value):
    """
    Check if value is a valid Chilean RUT ("rol único tributario")
    :param value: string
    :return:
    """
    try:
        if not chile_rut.validate_rut(value):
            raise ValidationError(
            _('RUT %s Invalid RUT'),
            params=value
        )
    except Exception as exc:
        raise ValidationError(
            _('RUT %s Invalid format'),
            params=value
        )


def validate_dose(value):
    """
    Check if the float value its between 0.15 and 1.0
    :param value: int | float
    :return:
    """
    if not 0.15 <= float(value) <= 1.0:
        raise ValidationError(
            _('dose: %s must be between 0.15 and 1.0'),
            params=value
        )
