#!-*-coding:utf-8-*-

from validathon.absent_field.decorator import AbsentFieldValidated
from validathon.result import ValidationResult
from validathon.validations.ivalidation import IValidation
from validathon.exceptions import ShouldBeIntExc
from typing import Any


@AbsentFieldValidated
class ShouldBeInt(IValidation):

    _exc: Exception
    _valid_msg: str

    def __init__(self, exc: Exception = None, valid_msg: str = ''):
        self._exc = exc
        self._valid_msg = valid_msg

    def validate(self, key: str, value: Any) -> ValidationResult:
        if not isinstance(value, int):
            if bool(self._exc):
                raise self._exc
            raise ShouldBeIntExc(
                ValidationResult(
                    field_name=key, msg=f'Field "{key}" must have a integer value.',
                    valid=False, validation=self
                )
            )
        return ValidationResult(field_name=key, msg=self._valid_msg, valid=True, validation=self)

    def __repr__(self):
        return 'ShouldBeInt()'
