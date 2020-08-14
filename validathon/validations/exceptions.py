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


class ShouldContainsOnlyCharsExc(ValidathonBaseException):
    pass


class MinLengthStrExc(ValidathonBaseException):
    pass


class MaxLengthStrExc(ValidathonBaseException):
    pass


class ShouldBeIntExc(ValidathonBaseException):
    pass


class CanNotBeAEmptyStrExc(ValidathonBaseException):
    pass


class CanNotBeNoneExc(ValidathonBaseException):
    pass


