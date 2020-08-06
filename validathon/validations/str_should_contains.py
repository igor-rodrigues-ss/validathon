

from typing import Any
from validathon.decorators.absent_field_validated import AbsentFieldValidated
from validathon.ivalidate import IValidation
from validathon.validations.exceptions import StrShouldContainsExc
from validathon.validation_result import ValidationResult


@AbsentFieldValidated
class StrShouldContains(IValidation):

    def __init__(self, string: str, exc: Exception = None, valid_msg: str = '', absent_field_exc: Exception = None):
        self._custom_exc = exc
        self._string = string
        self._valid_msg = valid_msg

    def validate(self, key: str, value: Any) -> ValidationResult:
        assert isinstance(value, str)
        if self._string not in value:
            if bool(self._custom_exc):
                raise self._custom_exc
            raise StrShouldContainsExc(
                ValidationResult(field=key, msg=f'Field "{key}" not contains "{self._string}".', valid=False)
            )
        return ValidationResult(field=key, msg=self._valid_msg, valid=True, validation=self)  # TODO: validation=self  necessry?

    def __repr__(self):
        if len(self._string) > 10:
            return f'StrShouldContains({self._string[0:10]}...)'
        return f'StrShouldContains({self._string})'
