#!-*-coding:utf-8-*-

import pytest
from validathon.validations import ShouldContainsOnlyChars
from validathon.result import ValidationResult
from validathon.exceptions import ShouldContainsOnlyCharsExc, FieldDoesNotExistsExc
from validathon.validator import Validator
from validathon.catch import Catch
from validathon.serialized import ValidationSerialized
from tests.conftest import CustomException


class TestShouldContainsOnlyChars:

    def test_validate_valid(self):
        data = {
            'name': 'abc'
        }
        vmap = {
            'name': ShouldContainsOnlyChars()
        }
        validator = Validator(vmap)
        result_map = validator.validate(data)
        assert 'name' in result_map.keys()
        assert isinstance(result_map['name'], ValidationResult)
        assert result_map['name'].field_name == 'name'
        assert result_map['name'].valid

    def test_validate_invalid_default(self):
        data = {
            'name': 'abc123'
        }
        vmap = {
            'name': ShouldContainsOnlyChars()
        }
        validator = Validator(vmap)
        with pytest.raises(ShouldContainsOnlyCharsExc) as exc:
            validator.validate(data)

        assert isinstance(exc.value.validation_result, ValidationResult)
        assert exc.value.validation_result.field_name == 'name'
        assert exc.value.validation_result.valid is False


    def test_validate_invalid_custom_exc(self):
        data = {
            'name': 'abc123'
        }
        vmap = {
            'name': ShouldContainsOnlyChars(exc=CustomException('Testing'))
        }
        validator = Validator(vmap)
        with pytest.raises(CustomException):
            validator.validate(data)

    def test_validate_invalid_catch(self):
        exc_msg = 'Testing'
        data = {
            'name': 'abc###'
        }
        vmap = {
            'name': Catch(ShouldContainsOnlyChars(exc=CustomException(exc_msg)))
        }
        validator = Validator(vmap)
        result_map = validator.validate(data)
        assert 'name' in result_map.keys()
        assert result_map['name'].field_name == 'name'
        assert result_map['name'].valid is False
        assert result_map['name'].msg == exc_msg

    def test_validate_inexisting_field(self):
        data = {
            'name_diff': 'abcabc'
        }
        vmap = {
            'name': ShouldContainsOnlyChars()
        }
        validator = Validator(vmap)
        with pytest.raises(FieldDoesNotExistsExc):
            validator.validate(data)

    def test_validate_absent_field_custom_exc(self):
        data = {
            'name_diff': 'abcabc'
        }
        vmap = {
            'name': ShouldContainsOnlyChars(required_exc=CustomException('Test'))
        }
        validator = Validator(vmap)
        with pytest.raises(CustomException):
            validator.validate(data)

    def test_validate_absent_field_cacth(self):
        exc_msg = 'Testing'
        data = {
            'name_diff': ''
        }
        vmap = {
            'name': Catch(ShouldContainsOnlyChars(required_exc=CustomException(exc_msg)))
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
            'name': {
                'name1': 'abc',
                'name2': 'abc',
                'name3': 'abc'
            }
        }
        vmap = {
            'name': {
                'name1': ShouldContainsOnlyChars(valid_msg=valid_msg1),
                'name2': ShouldContainsOnlyChars(valid_msg=valid_msg2),
                'name3': [ShouldContainsOnlyChars(valid_msg=valid_msg1)]

            }
        }
        validator = Validator(vmap)
        result_map = validator.validate(data)
        map_msgs = ValidationSerialized().map_msgs(result_map, root=True)
        assert 'name.name1' in map_msgs.keys()
        assert 'name.name2' in map_msgs.keys()
        assert 'name.name3' in map_msgs.keys()
        assert map_msgs['name.name1'] == valid_msg1
        assert map_msgs['name.name2'] == valid_msg2
        assert map_msgs['name.name3'][0] == valid_msg1

    def test_not_validate_if_absent_field(self):
        data = {
            'name': 'abcabc'
        }
        vmap = {
            'name1': ShouldContainsOnlyChars(required=False)
        }
        validator = Validator(vmap)
        result_map = validator.validate(data)
        assert 'name1' in result_map.keys()
        assert result_map['name1'].valid is None
        assert result_map['name1'].field_name is 'name1'
