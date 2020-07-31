

from typing import Any
from validathon.ivalidate import IValidation
from validathon.validations.exceptions import StrShouldContainsExc
from validathon.validation_result import ValidationResult


class StrShouldContains(IValidation):

    _field_does_not_exists_exc: Exception

    def __init__(self, string: str, custom_exc: Exception=None, field_does_not_exists_exc: Exception = None):
        self._field_does_not_exists_exc = field_does_not_exists_exc
        self._custom_exc = custom_exc
        self._string = string

    def validate(self, key: str, value: Any):
        super().field_does_not_exists(key, value, self._field_does_not_exists_exc)
        assert isinstance(value, str)
        if self._string not in value:
            if bool(self._custom_exc):
                raise self._custom_exc
            raise StrShouldContainsExc(
                ValidationResult(field=key, msg=f'Field "{key}" not contains "{self._string}".', valid=False)
            )
