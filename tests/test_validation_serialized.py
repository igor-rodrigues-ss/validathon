#!-*-coding:utf-8-*-
from validathon import StrShouldContains, ValidationSerialized, Catch
from validathon.validator import Validator
from tests.conftest import CustomException
from validathon.vtypes import VALIDATION_VALID, VALIDATION_INVALID


class TestValidationSerialized:

    def setup_method(self):
        self.valid_msg1 = 'Is Valid 1'
        self.valid_msg2 = 'Is Valid 2'
        self.invalid_mg1 = 'Invalid 1'
        data = {
            'name': {
                'name1': 'abcabc',
                'name2': 'abc-abc',
                'name3': 'abc-abc'
            }
        }
        vmap = {
            'name': {
                'name1': Catch(StrShouldContains('-', exc=CustomException(self.invalid_mg1), valid_msg=self.valid_msg1)),
                'name2': StrShouldContains('-', valid_msg=self.valid_msg2),
                'name3': [
                    StrShouldContains('-', valid_msg=self.valid_msg1),
                    StrShouldContains('-', valid_msg=self.valid_msg2)
                ]

            }
        }
        self.result_map = Validator(vmap).validate(data)

    def test_field_and_msgs_root_true_valid_invalid(self):
        vmp = ValidationSerialized().map_msgs(self.result_map, root=True)
        assert 'name.name1' in vmp.keys()
        assert 'name.name2' in vmp.keys()
        assert 'name.name3' in vmp.keys()
        assert vmp['name.name1'] == self.invalid_mg1
        assert vmp['name.name2'] == self.valid_msg2
        assert vmp['name.name3'][0] == self.valid_msg1
        assert vmp['name.name3'][1] == self.valid_msg2

    def test_field_and_msgs_root_false_valid_invalid(self):
        map_msg = ValidationSerialized().map_msgs(self.result_map, root=False)
        assert 'name' in map_msg.keys()
        assert 'name1' in map_msg['name'].keys()
        assert 'name2' in map_msg['name'].keys()
        assert 'name3' in map_msg['name'].keys()
        assert map_msg['name']['name1'] == self.invalid_mg1
        assert map_msg['name']['name2'] == self.valid_msg2
        assert map_msg['name']['name3'][0] == self.valid_msg1
        assert map_msg['name']['name3'][1] == self.valid_msg2

    def test_field_and_msgs_root_true_valid(self):
        map_msg = ValidationSerialized().map_msgs(self.result_map, root=True, only=VALIDATION_VALID)
        assert 'name.name1' not in map_msg.keys()  # This is invalid
        assert 'name.name2' in map_msg.keys()
        assert 'name.name3' in map_msg.keys()

    def test_field_and_msgs_root_true_invalid(self):
        map_msg = ValidationSerialized().map_msgs(self.result_map, root=True, only=VALIDATION_INVALID)
        assert 'name.name1' in map_msg.keys()
        assert 'name.name2' not in map_msg.keys()  # This is valid
        assert 'name.name3' not in map_msg.keys()  # This is valid
