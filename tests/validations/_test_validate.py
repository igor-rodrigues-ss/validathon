#!-*-coding:utf-8-*-

import pytest
from validathon import MinLengthStr, MaxLengthStr, ShouldBeInt, CanNotBeAEmptyStr
from validathon import CanNotBeNone
from validathon.exceptions import (
    MinLengthStrExc, ShouldBeIntExc, CanNotBeAEmptyStrExc, CanNotBeNoneExc, MaxLengthStrExc
)
from validathon import Validate


class CustomException(Exception):
    pass


class TestValidate:


    def test_validate_should_be_integer(self):
        data = {
            'name': 'abc'
        }
        validation_map = {
            'name': [ShouldBeInt()]
        }
        with pytest.raises(ShouldBeIntExc):
            Validate(data, validation_map).validate()

    def test_validate_should_be_integer_exc(self):
        data = {
            'name': 'abc'
        }
        validation_map = {
            'name': [ShouldBeInt(custom_exc=CustomException())]
        }
        with pytest.raises(CustomException):
            Validate(data, validation_map).validate()

    def test_validate_can_not_be_a_empty_str(self):
        data = {
            'name': ''
        }
        validation_map = {
            'name': [CanNotBeAEmptyStr()]
        }
        with pytest.raises(CanNotBeAEmptyStrExc):
            Validate(data, validation_map).validate()

    def test_validate_can_not_be_a_empty_str_exc(self):
        data = {
            'name': ''
        }
        validation_map = {
            'name': [CanNotBeAEmptyStr(custom_exc=CustomException())]
        }
        with pytest.raises(CustomException):
            Validate(data, validation_map).validate()


    def test_validate_can_not_be_none(self):
        data = {
            'name': None
        }
        validation_map = {
            'name': [CanNotBeNone()]
        }
        with pytest.raises(CanNotBeNoneExc):
            Validate(data, validation_map).validate()

    def test_validate_can_not_be_none_exc(self):
        data = {
            'name': None
        }
        validation_map = {
            'name': [CanNotBeNone(custom_exc=CustomException())]
        }
        with pytest.raises(CustomException):
            Validate(data, validation_map).validate()

