#!-*-coding:utf-8-*-
from validathon.serialized.types import VALIDATION_VALID, VALIDATION_INVALID, VALIDATION_VALID_INVALID


class ValidationSerialized:

    def create_list(self, output, v):
        if v.field not in output.keys():
            output[v.field] = []

    def _validate(self, data: dict, output: dict, root: bool, serialize_type: str): # TODO: create a enum serialize_type

        for k, v in data.items():
            if isinstance(v, dict):
                if root:
                    self._validate(v, output, root, serialize_type)
                else:
                    output[k] = {}
                    self._validate(v, output[k], root, serialize_type)
            else:
                if isinstance(v, list) or isinstance(v, tuple):
                    for validation_result in v:
                        if serialize_type == VALIDATION_VALID:
                            if validation_result.valid:
                                if root:
                                    self.create_list(output, v[0])
                                    output[v[0].field].append(validation_result.msg)
                                else:
                                    if k not in output.keys():
                                        output[k] = []
                                    output[k].append(validation_result.msg)

                        elif serialize_type == VALIDATION_INVALID:
                            if validation_result.valid is False:
                                if root:
                                    self.create_list(output, v[0])
                                    output[v[0].field].append(validation_result.msg)
                                else:
                                    if k not in output.keys():
                                        output[k] = []
                                    output[k].append(validation_result.msg)
                        else:
                            if root:
                                self.create_list(output, v[0])
                                output[v[0].field].append(validation_result.msg)
                            else:
                                if k not in output.keys():
                                    output[k] = []
                                output[k].append(validation_result.msg)

                else:
                    if serialize_type == VALIDATION_VALID:
                        if v.valid:
                            if root:
                                output[v.field] = v.msg
                            else:
                                output[k] = v.msg

                    elif serialize_type == VALIDATION_INVALID:
                        if v.valid is False:
                            if root:
                                output[v.field] = v.msg
                            else:
                                output[k] = v.msg
                    else:
                        if root:
                            output[v.field] = v.msg
                        else:
                            output[k] = v.msg

    def map_msgs(self, data: dict, root=True, only: str = VALIDATION_VALID_INVALID) -> dict:
        out = {}
        assert only in [VALIDATION_VALID, VALIDATION_INVALID, VALIDATION_VALID_INVALID], \
            '"only" variable with incorrect value, please use some of types VALIDATION_VALID, VALIDATION_INVALID,'\
            ' VALIDATION_VALID_INVALID from package validathon.types'
        self._validate(data, out, root, only)
        return out