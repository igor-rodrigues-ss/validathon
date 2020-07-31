#!-*-coding:utf-8-*-

from validathon.ivalidate import IValidation
from validathon.exceptions import MinLengthStrExc
from typing import Any


class MinLengthStr(IValidation):

    _custom_exc: Exception
    _min_len: int

    def __init__(self, min_len: int, custom_exc: Exception=None):
        self._custom_exc = custom_exc
        self._min_len = min_len

    def validate(self, key: str, value: Any):
        if len(value) < self._min_len:
            if bool(self._custom_exc):
                raise self._custom_exc
            raise MinLengthStrExc(f'Field "{key}" must be at least "{self._min_len}" characters.')
