#!-*-coding:utf-8-*-
from validathon.decorators.absent_field_validated import AbsentFieldValidated
from validathon.result import ValidationResult
from validathon.validations.ivalidation import IValidation
from validathon.exceptions import CanNotBeNoneExc
from typing import Any


@AbsentFieldValidated
class CanNotBeNone(IValidation):

    _exc: Exception

    def __init__(self, exc: Exception = None, valid_msg: str = ''):
        self._exc = exc
        self._valid_msg = valid_msg

    def validate(self, key: str, value: Any):
        if value is None:
            if bool(self._exc):
                raise self._exc
            raise CanNotBeNoneExc(f'Field "{key}" cannot have a None value.')
        return ValidationResult(field_name=key, msg=self._valid_msg, valid=True, validation=self)

