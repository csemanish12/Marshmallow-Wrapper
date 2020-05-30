class MarshmallowV2:
    @classmethod
    def dump(cls, objects, schema, **kwargs):
        required_schema = cls.get_schema(schema, **kwargs)
        result, errors = required_schema.dump(objects)
        return result

    @classmethod
    def load(cls, data, schema, **kwargs):
        required_schema = cls.get_schema(schema, **kwargs)
        result, errors = required_schema.load(data)
        return result

    @classmethod
    def get_schema(cls, schema_name, **kwargs):
        """
        developers/collaborators will always use the predefined keys in serializers
        we can define these keys in our coding standards
        therefore, we can adjust the parameters name as per library being used for serialization by changing just
        this method.
        eg: marshmallow uses strict=True parameter raise error for validation
        lets say, we use SomeOtherLibrary for serialization which use raise_error=True for raising validation error
        then we can simply change the key being passed in the Schema.

        :param schema_name: schema class
        :param kwargs:
        :return:
        """
        multiple = kwargs.get('many', None)
        dump_only = kwargs.get('dump_only', None)
        only = kwargs.get('only', None)
        load_only = kwargs.get('load_oly', None)
        exclude = kwargs.get('exclude', None)
        partial = kwargs.get('partial', None)
        instance = kwargs.get('instance', None)
        session = kwargs.get('session', None)

        keyword_parameters = {}
        keyword_parameters.update({"strict": True})
        if multiple is not None:
            keyword_parameters.update(({"many": True}))
        if dump_only is not None:
            keyword_parameters.update(({"dump_only": dump_only}))
        if only is not None:
            keyword_parameters.update(({"only": only}))
        if load_only is not None:
            keyword_parameters.update(({"load_only": load_only}))
        if exclude is not None:
            keyword_parameters.update(({"exclude": exclude}))
        if partial is not None:
            keyword_parameters.update(({"partial": partial}))
        if instance is not None:
            keyword_parameters.update(({"instance": instance}))
        if session is not None:
            keyword_parameters.update({"session": session})

        if keyword_parameters == {}:
            return schema_name()
        return schema_name(**keyword_parameters)