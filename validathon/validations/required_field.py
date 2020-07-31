

from typing import Any
from validathon.ivalidate import IValidation, REQUIRED_KEY # trocar este nome para chave não existe
from validathon.validations.exceptions import RequiredExc  # passar para o exception raiz
from validathon.validation_result import ValidationResult


class Required(IValidation):

    _custom_exc: Exception

    def __init__(self, custom_exc: Exception = None):
        self._custom_exc = custom_exc

    def validate(self, key: str, value: Any):
        if value == REQUIRED_KEY:
            if bool(self._custom_exc):
                raise self._custom_exc
            raise RequiredExc(
                ValidationResult(field=key, msg=f'Field "{key}" does not exists.', valid=False)
            )