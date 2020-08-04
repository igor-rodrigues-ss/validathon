
from validathon.validations.str_should_contains import StrShouldContains
from validathon.ivalidate import REQUIRED_KEY
from validathon.validations.required import Required
from validathon import Catch


"""
- Caso exista algum chave em dados que não exista no mapa de validação e a variável "map_should_be_identical"
estiver com valor false, a validação deste campo não será realizada
"""

class Validathon:

    _val_map: dict

    def __init__(self, val_map: dict):
        self._val_map = val_map

    def _father_field(self, old_key: str, new_key: str):
        if old_key == '':
            return new_key
        return old_key + '.' + new_key

    def _validate(self, data: dict, validation_map: dict, out_v_map: dict={}, path_keys: str=''):
        # TODO: validar se chaves estão escritas com nome errado

        for key_map, validations in validation_map.items():
            path_keys = self._father_field(path_keys, key_map)
            item_to_val = data.get(key_map, REQUIRED_KEY)

            if isinstance(validations, dict):
                out_v_map[key_map] = {}
                self._validate(item_to_val, validations, out_v_map[key_map], path_keys)
                break

            if isinstance(validations, list) or isinstance(validations, tuple):
                out_v_map[key_map] = []
                for validation in validations:
                    out_v_map[key_map].append(validation.validate(path_keys, item_to_val))
            else:
                out_v_map[key_map] = validations.validate(path_keys, item_to_val)

    def validate(self, data: dict) -> dict:
        assert isinstance(data, dict), '"data" should be a dict.'
        out_validation_map = {}
        self._validate(data, self._val_map, out_validation_map)
        return out_validation_map


if __name__ == '__main__':
    # validator = Validathon(
    #     {'name': {'aa': {
    #         # 'bbb': [RequiredField(), RequiredField()], 'cc': RequiredField()
    #         'bbb': [VR(RequiredField()), VR(DeverSerA(inexisting_field_exc=RequiredFieldExc(ValidationResult(field='name.aa.bbb', msg='campo não existe', valid=False))))], 'cc': VR(RequiredField())
    #     }}}
    # )

    validator = Validathon(
        {'name': {'aa': {
            # 'bbb': [RequiredField(), RequiredField()], 'cc': RequiredField()
            # 'bbb': [VR(RequiredField()), VR(DeverSerA(inexisting_field_exc=RequiredFieldExc(
            #     ValidationResult(field='name.aa.bbb', msg='campo não existe', valid=False))))],
            # 'cc': [Catch(Required(Exception('campo não exisste mlk'))), Catch(StrShouldContains('-'))]
            'cca': [Catch(Required(Exception('campo não exisste mlk'))), Catch(StrShouldContains('-'))]
        }}}
    )
     # TODO: criar testes unitários para campos que não existe



    # maps = validator.validate({'name': {'aa': {'bbb': 'aa', 'cc': 'aaa'}}})
    maps = validator.validate({'name': {'aa': {'cc': 'asdf-'}}})
    # maps = validator.validate({'name': {'aa': {'dd': 'asdf'}}})
    print(maps)
    # Validate(
    #     {
    #         'name': 'aaaá', 'teste': {
    #             'aaaa': 'aaa', 'teste2': {'bbb': '1'},
    #         }
    #     },
    #     {
    #         'name': [FieldMustBeContainsOnlyString()],
    #         'teste': {
    #             'aaaa': [FieldMustBeContainsOnlyString(), MinLengthStr(3)],
    #             'teste2': {
    #                 'bbb': [MinLengthStr(3)]
    #             }
    #         }
    #     }
    # ).validate()