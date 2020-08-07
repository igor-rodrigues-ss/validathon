#!-*-coding:utf-8-*-

from validathon.result import ValidationResult


class ValidathonBaseException(Exception):

    validation_result: ValidationResult

    def __init__(self, validation_result: ValidationResult):
        self.validation_result = validation_result
        super().__init__(validation_result.msg)


class FieldDoesNotExistsExc(ValidathonBaseException):
    pass


class StrShouldContainsExc(ValidathonBaseException):
    pass


class RequiredExc(ValidathonBaseException):
    pass


class ShouldContainsOnlyCharsExc(Exception):
    pass


class MinLengthStrExc(Exception):
    pass


class MaxLengthStrExc(Exception):
    pass


class ShouldBeIntExc(Exception):
    pass


class CanNotBeAEmptyStrExc(Exception):
    pass


class CanNotBeNoneExc(Exception):
    pass


class ShouldBeAValidEmailExc(Exception):
    pass


