#!-*-coding:utf-8-*-

from abc import ABC, abstractmethod
from typing import Any
from validathon.validations.exceptions import ValidathonBaseException
from validathon.validation_result import ValidationResult

REQUIRED_KEY = 'campo_não_existe_123456'


class FieldDoesNotExistsExc(ValidathonBaseException):
    pass


class IValidation(ABC):

    def field_does_not_exists(self, key, value, field_does_not_exists_exc: Exception):
        if value == REQUIRED_KEY:
            if bool(field_does_not_exists_exc):
                raise field_does_not_exists_exc
            raise FieldDoesNotExistsExc(
                ValidationResult(field=key, msg=f'Não validado, campo "{key}" inexistente.', valid=False)
            )

    @abstractmethod
    def validate(self, key: str, value: Any):
        pass
