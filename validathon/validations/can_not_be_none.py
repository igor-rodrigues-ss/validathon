#!-*-coding:utf-8-*-

from validathon.ivalidate import IValidation
from validathon.exceptions import CanNotBeNoneExc
from typing import Any


class CanNotBeNone(IValidation):

    _custom_exc: Exception

    def __init__(self, custom_exc: Exception=None):
        self._custom_exc = custom_exc

    def validate(self, key: str, value: Any):
        if value is None:
            if bool(self._custom_exc):
                raise self._custom_exc
            raise CanNotBeNoneExc(f'Field "{key}" cannot have a None value.')
