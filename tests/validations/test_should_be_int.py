#!-*-coding:utf-8-*-

import pytest
from validathon.validations import ShouldBeInt
from validathon.result import ValidationResult
from validathon.exceptions import ShouldBeIntExc, FieldDoesNotExistsExc
from validathon.validator import Validator
from validathon.catch import Catch
from validathon.serialized import ValidationSerialized
from tests.conftest import CustomException


class TestShouldBeInt:

    def test_validate_valid(self):
        data = {
            'num': 1
        }
        vmap = {
            'num': ShouldBeInt()
        }
        validator = Validator(vmap)
        result_map = validator.validate(data)
        assert 'num' in result_map.keys()
        assert isinstance(result_map['num'], ValidationResult)
        assert result_map['num'].field_name == 'num'
        assert result_map['num'].valid

    def test_validate_invalid_default(self):
        data = {
            'num': 'ab'
        }
        vmap = {
            'num': ShouldBeInt()
        }
        validator = Validator(vmap)
        with pytest.raises(ShouldBeIntExc) as exc:
            validator.validate(data)

        assert isinstance(exc.value.validation_result, ValidationResult)
        assert exc.value.validation_result.field_name == 'num'
        assert exc.value.validation_result.valid is False

    def test_validate_invalid_custom_exc(self):
        data = {
            'num': 'abc'
        }
        vmap = {
            'num': ShouldBeInt(exc=CustomException('Testing'))
        }
        validator = Validator(vmap)
        with pytest.raises(CustomException):
            validator.validate(data)

    def test_validate_invalid_catch(self):
        exc_msg = 'Testing'
        data = {
            'name': 'abc'
        }
        vmap = {
            'name': Catch(ShouldBeInt(exc=CustomException(exc_msg)))
        }
        validator = Validator(vmap)
        result_map = validator.validate(data)
        assert 'name' in result_map.keys()
        assert result_map['name'].field_name == 'name'
        assert result_map['name'].valid is False
        assert result_map['name'].msg == exc_msg

    def test_validate_inexisting_field(self):
        data = {
            'name_diff': 'ab'
        }
        vmap = {
            'name': ShouldBeInt()
        }
        validator = Validator(vmap)
        with pytest.raises(FieldDoesNotExistsExc):
            validator.validate(data)

    def test_validate_absent_field_custom_exc(self):
        data = {
            'name_diff': 'abc'
        }
        vmap = {
            'name': ShouldBeInt(required_exc=CustomException('Test'))
        }
        validator = Validator(vmap)
        with pytest.raises(CustomException):
            validator.validate(data)

    def test_validate_absent_field_cacth(self):
        exc_msg = 'Testing'
        data = {
            'name_diff': 'abc'
        }
        vmap = {
            'name': Catch(ShouldBeInt(required_exc=CustomException(exc_msg)))
        }
        validator = Validator(vmap)
        result_map = validator.validate(data)
        assert 'name' in result_map.keys()
        assert result_map['name'].field_name == 'name'
        assert result_map['name'].valid is False
        assert result_map['name'].msg == exc_msg

    def test_validate_serialized(self):
        valid_msg1 = 'Is Valid 1'
        valid_msg2 = 'Is Valid 2'
        data = {
            'num': {
                'num1': 123,
                'num2': 232,
                'num3': 33,
            }
        }
        vmap = {
            'num': {
                'num1': ShouldBeInt(valid_msg=valid_msg1),
                'num2': ShouldBeInt(valid_msg=valid_msg2),
                'num3': [ShouldBeInt(valid_msg=valid_msg1)]

            }
        }
        validator = Validator(vmap)
        result_map = validator.validate(data)
        map_msgs = ValidationSerialized().map_msgs(result_map, root=True)
        assert 'num.num1' in map_msgs.keys()
        assert 'num.num2' in map_msgs.keys()
        assert 'num.num3' in map_msgs.keys()
        assert map_msgs['num.num1'] == valid_msg1
        assert map_msgs['num.num2'] == valid_msg2
        assert map_msgs['num.num3'][0] == valid_msg1

    def test_not_validate_if_absent_field(self):
        data = {
            'num': 123
        }
        vmap = {
            'num1': ShouldBeInt(required=False)
        }
        validator = Validator(vmap)
        result_map = validator.validate(data)
        assert 'num1' in result_map.keys()
        assert result_map['num1'].valid is None
        assert result_map['num1'].field_name == 'num1'
