#!-*-coding:utf-8-*-

from validathon.absent_field.decorator import AbsentFieldValidated
from validathon.result import ValidationResult
from validathon.validations.ivalidation import IValidation
from validathon.exceptions import MinLengthStrExc
from typing import Any


@AbsentFieldValidated
class MinLengthStr(IValidation):

    _exc: Exception
    _min_len: int
    _valid_msg: str

    def __init__(self, min_len: int, exc: Exception = None, valid_msg: str = ''):
        self._exc = exc
        self._min_len = min_len
        self._valid_msg = valid_msg

    def validate(self, key: str, value: Any) -> ValidationResult:
        if len(value) < self._min_len:
            if bool(self._exc):
                raise self._exc
            raise MinLengthStrExc(f'Field "{key}" must be at least "{self._min_len}" characters.')
        return ValidationResult(field_name=key, msg=self._valid_msg, valid=True, validation=self)

    def __repr__(self):
        return f'MinLengthStr({self._min_len})'
