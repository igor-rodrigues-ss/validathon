#!-*-coding:utf-8-*-

from validathon.ivalidate import IValidation
from validathon.exceptions import MaxLengthStrExc
from typing import Any


class MaxLengthStr(IValidation):

    _custom_exc: Exception
    _min_len: int

    def __init__(self, min_len: int, custom_exc: Exception=None):
        self._custom_exc = custom_exc
        self._max_len = min_len

    def validate(self, key: str, value: Any):
        if len(value) > self._max_len:
            if bool(self._custom_exc):
                raise self._custom_exc
            raise MaxLengthStrExc(f'Field "{key}" should be contains at most "{self._max_len}" characters.')
