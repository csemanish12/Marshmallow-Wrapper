import os

from wrappers.marshmallow.marshmallow_v2 import MarshmallowV2
from wrappers.marshmallow.marshmallow_v3 import MarshmallowV3


class MarshmallowVersionManager:
    @classmethod
    def get_marshmallow(cls):
        if os.environ.get('MARSHMALLOW') == 'V2':
            return MarshmallowV2
        else:
            return MarshmallowV3