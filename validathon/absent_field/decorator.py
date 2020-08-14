#!-*-coding:utf-8-*-

from validathon.absent_field.ignored import AbsentFieldIgnored
from validathon.validations.ivalidation import IValidation
from validathon.absent_field.validated import AbsentFieldValidated as AbsentFieldValidatedImpl


class AbsentFieldValidated:

    _validation_clss: IValidation

    def __init__(self, clss: IValidation):
        self._validation_clss = clss

    def __call__(self, *args, **kwargs):
        required_exc = None
        required = True

        if 'required_exc' in kwargs.keys():
            required_exc = kwargs.pop('required_exc')

        if 'required' in kwargs.keys():
            required = kwargs.pop('required')

        if required:
            return AbsentFieldValidatedImpl(
                self._validation_clss(*args, **kwargs), required_exc
            )
        return AbsentFieldIgnored(
            self._validation_clss(*args, **kwargs)
        )
