#!-*-coding:utf-8-*-

import pytest
from validathon import MinLengthStr
from validathon.exceptions import MinLengthStrExc
from validathon import Validate


class CustomException(Exception):
    pass


class TestMinLengthStr:

    def test_validate_str_min_len(self):
        data = {
            'name': 'jão'
        }
        validation_map = {
            'name': [MinLengthStr(4)]
        }
        with pytest.raises(MinLengthStrExc):
            Validate(data, validation_map).validate()

    def test_validate_str_min_len_custom_exc(self):
        data = {
            'name': 'jão'
        }
        validation_map = {
            'name': [MinLengthStr(4, custom_exc=CustomException())]
        }
        with pytest.raises(CustomException):
            Validate(data, validation_map).validate()
