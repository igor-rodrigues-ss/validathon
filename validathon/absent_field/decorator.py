#!-*-coding:utf-8-*-

from validathon.absent_field.ignored import AbsentFieldIgnored
from validathon.validations.ivalidation import IValidation
from validathon.absent_field.validated import AbsentFieldValidated as AbsentFieldValidatedImpl


class AbsentFieldValidated:

    _validation_clss: IValidation

    def __init__(self, clss: IValidation):
        self._validation_clss = clss

    def __call__(self, *args, **kwargs):
        absent_field_exc = None
        validate_for_absent = True

        if 'absent_field_exc' in kwargs.keys():
            absent_field_exc = kwargs.pop('absent_field_exc')

        if 'validate_for_absent' in kwargs.keys():
            validate_for_absent = kwargs.pop('validate_for_absent')

        if validate_for_absent:
            return AbsentFieldValidatedImpl(
                self._validation_clss(*args, **kwargs), absent_field_exc
            )
        return AbsentFieldIgnored(
            self._validation_clss(*args, **kwargs)
        )
