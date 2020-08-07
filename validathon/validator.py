

from validathon.config import REQUIRED_KEY


"""
- Caso exista algum chave em dados que não exista no mapa de validação e a variável "map_should_be_identical"
estiver com valor false, a validação deste campo não será realizada
"""

class Validator:

    _val_map: dict

    def __init__(self, val_map: dict):
        self._val_map = val_map

    def _father_field(self, old_key: str, new_key: str):
        if old_key == '':
            return new_key
        return old_key + '.' + new_key

    def _validate(self, data: dict, validation_map: dict, out_v_map: dict = {}, path_keys: str = ''):
        # TODO: validar se chaves estão escritas com nome errado
        old_key = path_keys
        for key_map, validations in validation_map.items():
            path_keys = self._father_field(old_key, key_map)
            item_to_val = data.get(key_map, REQUIRED_KEY)

            if isinstance(validations, dict):

                out_v_map[key_map] = {}
                self._validate(item_to_val, validations, out_v_map[key_map], path_keys)
            else:
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

    from validathon import StrShouldContains
    vmap = {
        'name': StrShouldContains('-', raise_absent_field=False) # Create unity tests for this argument
    }
    data = {
        'name1': 'abc-'
    }
    validator = Validator(vmap)
    print(validator.validate(data))