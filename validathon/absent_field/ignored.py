#!-*-coding:utf-8-*-

from validathon.validations.ivalidation import IValidation
from validathon.result import ValidationResult
from typing import Type, Any
from validathon.config import VALUE_FOR_ABSENT_FIELD


class AbsentFieldIgnored(IValidation):

    _validation: Type[IValidation]

    def __init__(self, validation: Type[IValidation]):
        self._validation = validation

    def validate(self, key: str, value: Any) -> ValidationResult:
        if value == VALUE_FOR_ABSENT_FIELD:
            return ValidationResult(
                field_name=key, msg=f'Not Validated. Field "{key}" does not exists.',
                valid=None, validation=self._validation
            )
        return self._validation.validate(key, value)
