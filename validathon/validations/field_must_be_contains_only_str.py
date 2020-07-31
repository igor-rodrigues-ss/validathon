#!-*-coding:utf-8-*-

from validathon.ivalidate import IValidation
from validathon.exceptions import FieldMustNotBeContainsNumbersExc
from typing import Any


class FieldMustBeContainsOnlyString(IValidation):

    _custom_exc: Exception

    def __init__(self, custom_exc: Exception=None):
        self._custom_exc = custom_exc

    def validate(self, key: str, value: Any):
        value = str(value)
        if not value.isalpha():
            if bool(self._custom_exc):
                raise self._custom_exc
            raise FieldMustNotBeContainsNumbersExc(f'Field "{key}" must not be contains numbers.')
