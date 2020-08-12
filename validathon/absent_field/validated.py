#!-*-coding:utf-8-*-

from typing import Type, Any
from validathon.validations.ivalidation import IValidation
from validathon.result import ValidationResult
from validathon.validations.exceptions import FieldDoesNotExistsExc
from validathon.config import VALUE_FOR_ABSENT_FIELD


class AbsentFieldValidated(IValidation):

    _validation: Type[IValidation]
    _required_exc: Exception

    def __init__(self, validation: Type[IValidation], required_exc: Exception = None):
        self._validation = validation
        self._required_exc = required_exc

    def _field_does_not_exists(self, key, value):
        if value == VALUE_FOR_ABSENT_FIELD:
            if bool(self._required_exc):
                raise self._required_exc
            raise FieldDoesNotExistsExc(
                ValidationResult(field_name=key, msg=f'Not validated. Field "{key}" does not exists.', valid=False)
            )

    def validate(self, key: str, value: Any):
        self._field_does_not_exists(key, value)
        return self._validation.validate(key, value)

    def __repr__(self):
        return f'AbsentFieldValidated({self._validation.__repr__()})'
