from validathon.ivalidate import IValidation
from validathon.validation_result import ValidationResult
from validathon.validations.exceptions import FieldDoesNotExistsExc
from typing import Type
from validathon.config import REQUIRED_KEY


class AbsentFieldValidatedInner(IValidation):

    def __init__(self, validation: Type[IValidation], absent_field_exc: Exception = None):
        self._validation = validation
        self._absent_field_exc = absent_field_exc

    def _field_does_not_exists(self, key, value):
        if value == REQUIRED_KEY:
            if bool(self._absent_field_exc):
                raise self._absent_field_exc
            raise FieldDoesNotExistsExc(
                ValidationResult(field=key, msg=f'Não validado, campo "{key}" inexistente.', valid=False)
            )

    def validate(self, key, value):
        self._field_does_not_exists(key, value)  # TODO: criar testes unitários para validar essa função
        return self._validation.validate(key, value)

    def __repr__(self):
        return f'AbsentFieldValidated({self._validation.__repr__()})'


class AbsentFieldValidated:

    _validation_clss: IValidation

    def __init__(self, clss: IValidation):
        self._validation_clss = clss

    def __call__(self, *args, **kwargs):
        absent_field_exc = None
        if 'absent_field_exc' in kwargs.keys():
            absent_field_exc = kwargs.pop('absent_field_exc')
        return AbsentFieldValidatedInner(self._validation_clss(*args, **kwargs), absent_field_exc)
