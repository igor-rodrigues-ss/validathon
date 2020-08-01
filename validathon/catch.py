#!-*-coding:utf-8-*-

from validathon.validations.exceptions import ValidathonBaseException
from validathon.validation_result import ValidationResult
from validathon.ivalidate import IValidation


class Catch:

    def __init__(self, obj: IValidation):
        self.val_obj = obj

    def validate(self, *args, **kwargs) -> ValidationResult:
        try:
            return self.val_obj.validate(*args, **kwargs)
        except ValidathonBaseException as exc1:
            field = exc1.validation_result.field
            msg = exc1.validation_result.msg
            valid = exc1.validation_result.valid
            return ValidationResult(field=field, msg=msg, valid=valid, exc=exc1)
        except Exception as exc2:
            # TODO: colocar na documentação para que sempre que o desenvolvedor for lançar uma
            #  execção que seja derivada de ValidathonBaseException para não cair neste fluxo
            return ValidationResult(field=args[0], msg=str(exc2), valid=False, exc=exc2)
        else:
            return ValidationResult(field=args[0], msg='', valid=True)