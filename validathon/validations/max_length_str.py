#!-*-coding:utf-8-*-

from validathon.absent_field.decorator import AbsentFieldValidated
from validathon.result import ValidationResult
from validathon.validations.ivalidation import IValidation
from validathon.exceptions import MaxLengthStrExc
from typing import Any


@AbsentFieldValidated
class MaxLengthStr(IValidation):

    _exc: Exception
    _min_len: int
    _valid_msg: str

    def __init__(self, max_len: int, exc: Exception = None, valid_msg: str = ''):
        self._exc = exc
        self._max_len = max_len
        self._valid_msg = valid_msg

    def validate(self, key: str, value: Any) -> ValidationResult:
        if len(value) > self._max_len:
            if bool(self._exc):
                raise self._exc
            raise MaxLengthStrExc(f'Field "{key}" should be contains at most "{self._max_len}" characters.')
        return ValidationResult(field_name=key, msg=self._valid_msg, valid=True, validation=self)

    def __repr__(self):
        return f'MaxLengthStr({self._max_len})'
