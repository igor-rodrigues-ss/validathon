#!-*-coding:utf-8-*-
from validathon.absent_field.decorator import AbsentFieldValidated
from validathon.result import ValidationResult
from validathon.validations.ivalidation import IValidation
from validathon.exceptions import CanNotBeAEmptyStrExc
from typing import Any


@AbsentFieldValidated
class CanNotBeAEmptyStr(IValidation):

    _exc: Exception
    _valid_msg: str

    def __init__(self, exc: Exception = None, valid_msg: str = ''):
        self._exc = exc
        self._valid_msg = valid_msg

    def validate(self, key: str, value: Any) -> ValidationResult:
        if value == '':
            if bool(self._exc):
                raise self._exc
            raise CanNotBeAEmptyStrExc(
                ValidationResult(
                    field_name=key, msg=f'Field "{key}" can not be a empty string.',
                    valid=False, validation=self
                )
            )
        return ValidationResult(field_name=key, msg=self._valid_msg, valid=True, validation=self)

    def __repr__(self):
        return "CanNotBeAEmptyStr()"
