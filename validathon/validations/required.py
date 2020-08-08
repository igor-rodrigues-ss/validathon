

from typing import Any
from validathon.validations.ivalidation import IValidation
from validathon.validations.exceptions import RequiredExc
from validathon.result import ValidationResult
from validathon.config import VALUE_FOR_ABSENT_FIELD


class Required(IValidation):

    _custom_exc: Exception

    def __init__(self, exc: Exception = None, valid_msg=''):
        self._custom_exc = exc
        self._valid_msg = valid_msg

    def validate(self, key: str, value: Any) -> ValidationResult:
        if value == VALUE_FOR_ABSENT_FIELD:
            if bool(self._custom_exc):
                raise self._custom_exc
            raise RequiredExc(
                ValidationResult(field=key, msg=f'Field "{key}" does not exists.', valid=False)
            )
        return ValidationResult(field=key, msg=self._valid_msg, valid=True, validation=self)
