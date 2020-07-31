#!-*-coding:utf-8-*-

import pytest
from validathon import MaxLengthStr
from validathon.exceptions import MaxLengthStrExc
from validathon import Validate


class CustomException(Exception):
    pass


class TestMaxLengthStr:

    def test_validate_str_max_len(self):
        data = {
            'name': 'aaaaaaaaaa'
        }
        validation_map = {
            'name': [MaxLengthStr(4)]
        }
        with pytest.raises(MaxLengthStrExc):
            Validate(data, validation_map).validate()

    def test_validate_str_max_len_custom_exc(self):
        data = {
            'name': 'aaaaaaaaaa'
        }
        validation_map = {
            'name': [MaxLengthStr(4, custom_exc=CustomException())]
        }
        with pytest.raises(CustomException):
            Validate(data, validation_map).validate()
