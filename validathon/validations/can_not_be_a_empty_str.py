#!-*-coding:utf-8-*-

from validathon.ivalidate import IValidation
from validathon.exceptions import CanNotBeAEmptyStrExc
from typing import Any


class CanNotBeAEmptyStr(IValidation):

    _custom_exc: Exception

    def __init__(self, custom_exc: Exception=None):
        self._custom_exc = custom_exc

    def validate(self, key: str, value: Any):
        if value == '':
            if bool(self._custom_exc):
                raise self._custom_exc
            raise CanNotBeAEmptyStrExc(f'Field "{key}" can not be a empty string.')
