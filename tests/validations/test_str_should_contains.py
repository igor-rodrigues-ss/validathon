

from validathon import StrShouldContains
from validathon.validation_result import ValidationResult
from validathon.exceptions import StrShouldContainsExc, FieldDoesNotExistsExc
from validathon.main import Validathon
from validathon import Catch
import pytest


class CustomException(Exception):
    pass


class TestStrShouldContains:

    def test_validate_valid(self):
        data = {
            'name': 'abc-abc'
        }
        vmap = {
            'name': StrShouldContains('-')
        }
        validator = Validathon(vmap)
        result_map = validator.validate(data)
        assert 'name' in result_map.keys()
        assert isinstance(result_map['name'], ValidationResult)
        assert result_map['name'].field == 'name'
        assert result_map['name'].valid

    def test_validate_invalid_default(self):
        data = {
            'name': 'abcabc'
        }
        vmap = {
            'name': StrShouldContains('-')
        }
        validator = Validathon(vmap)
        with pytest.raises(StrShouldContainsExc):
            validator.validate(data)

    def test_validate_invalid_custom_exc(self):
        data = {
            'name': 'abcabc'
        }
        vmap = {
            'name': StrShouldContains('-', exc=CustomException('Testing'))
        }
        validator = Validathon(vmap)
        with pytest.raises(CustomException):
            validator.validate(data)

    def test_validate_invalid_catch(self):
        exc_msg = 'Testing'
        data = {
            'name': 'abcabc'
        }
        vmap = {
            'name': Catch(StrShouldContains('-', exc=CustomException(exc_msg)))
        }
        validator = Validathon(vmap)
        result_map = validator.validate(data)
        assert 'name' in result_map.keys()
        assert result_map['name'].field == 'name'
        assert result_map['name'].valid is False
        assert result_map['name'].msg == exc_msg

    def test_validate_inexisting_field(self):
        data = {
            'name_diff': 'abcabc'
        }
        vmap = {
            'name': StrShouldContains('-')
        }
        validator = Validathon(vmap)
        with pytest.raises(FieldDoesNotExistsExc):
            validator.validate(data)

    def test_validate_absent_field_custom(self):
        data = {
            'name_diff': 'abcabc'
        }
        vmap = {
            'name': StrShouldContains('-', absent_field_exc=CustomException('Test'))
        }
        validator = Validathon(vmap)
        with pytest.raises(CustomException):
            validator.validate(data)

    def test_validate_absent_field_cacth(self):
        exc_msg = 'Testing'
        data = {
            'name_diff': 'abcabc'
        }
        vmap = {
            'name': Catch(StrShouldContains('-', absent_field_exc=CustomException(exc_msg)))
        }
        validator = Validathon(vmap)
        result_map = validator.validate(data)
        assert 'name' in result_map.keys()
        assert result_map['name'].field == 'name'
        assert result_map['name'].valid is False
        assert result_map['name'].msg == exc_msg
