#!-*-coding:utf-8-*-

from validathon.validations.ivalidation import IValidation
from typing import Any


class ShouldBeAValidEmail(IValidation):

    _custom_exc: Exception
    _with_dot_com: bool

    def __init__(self, with_dot_com: bool=False, custom_exc: Exception=None):
        self._custom_exc = custom_exc
        self._with_dot_com = with_dot_com

    def validate(self, key: str, value: Any):
        value = str(value)
        a_symbol_count = value.count('@')
        if a_symbol_count == 0:
            raise Exception('Sem @')

        if a_symbol_count > 1:
            raise Exception('Deve possuir apenas 1 arroba')

        start_email, end_email = value.split('@')

        if start_email == '':
            raise Exception('Email invalido')

        if self._with_dot_com:
            if not value.endswith('.com'):
                raise Exception('email deve terminar com .com')

        if end_email == '.com':  # @.com
            raise Exception('Email invalido')
