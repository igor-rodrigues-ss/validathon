#!-*-coding:utf-8-*-

from validathon.ivalidate import IValidation
from validathon.exceptions import ShouldBeIntExc
from typing import Any


class ShouldBeInt(IValidation):

    _custom_exc: Exception

    def __init__(self, custom_exc: Exception=None):
        self._custom_exc = custom_exc

    def validate(self, key: str, value: Any):
        if not isinstance(value, int):
            if bool(self._custom_exc):
                raise self._custom_exc
            raise ShouldBeIntExc(f'Field "{key}" must have a integer value.')
