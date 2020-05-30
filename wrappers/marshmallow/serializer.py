from wrappers.marshmallow.marshmallow_manager import MarshmallowVersionManager


class Serializer:
    def __init__(self):
        self.serializer = MarshmallowVersionManager.get_marshmallow()

    def serialize(self, objects, schema, **kwargs):
        """
        Serialize objects by passing them to your schema’s dump method, which returns the formatted result.
        :return:
        """
        return self.serializer.dump(objects, schema, **kwargs)

    def deserialize(self, data, schema, **kwargs):
        """
        The reverse of the dump method is load, which validates and deserializes an input dictionary to an application-level data structure.
        :return:
        """
        return self.serializer.load(data, schema, **kwargs)