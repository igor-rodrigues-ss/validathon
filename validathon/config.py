#!-*-coding:utf-8-*-

from datetime import datetime
import random
import string


def absent_field_hash():
    dt = datetime.now().strftime('%Y%m%d%H%M%S')
    ascii_hash = ''.join(random.sample(string.ascii_letters, 4))
    punc_hash = ''.join(random.sample(string.punctuation, 4))
    return f'absent_field_hash_{dt}{ascii_hash}{punc_hash}'


VALUE_FOR_ABSENT_FIELD = absent_field_hash()
