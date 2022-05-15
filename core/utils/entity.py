from core.utils.general import adapt


class EntityMeta(type):
    def __new__(mcs, name, bases, cls_dict):
        cls_dict['_entities'] = dict()
        return super().__new__(mcs, name, bases, cls_dict)


class Entity(metaclass=EntityMeta):
    _entities = dict()
    _defaults = dict()

    _id = None

    def __new__(cls, **kwargs):
        obj_id = cls.get_id(**kwargs)
        if obj_id not in cls._entities:
            obj = super().__new__(cls)
            obj._id = obj_id
            cls._entities[obj_id] = obj
            return obj

    def __init__(self, **kwargs):
        adapt(self, self.__class__._defaults, **kwargs)

    @classmethod
    def remove(cls, obj_id):
        del cls._entities[obj_id]

    def destroy(self):
        self.__class__.remove(self._id)

    @classmethod
    def get_or_create(cls, **kwargs):
        obj_id = cls.get_id(**kwargs)
        return cls.get_by_id(obj_id) or cls(**kwargs)

    @classmethod
    def get_id(cls, **kwargs):
        return len(cls._entities) + 1

    @classmethod
    def get_by_id(cls, obj_id, safe=True):
        if safe:
            return cls._entities.get(obj_id)
        return cls._entities[obj_id]

    def register(self, obj_id):
        entities = self.__class__._entities
        entities.pop(self._id)
        entities[obj_id] = self
        self._id = obj_id

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'<{self.__class__.__name__} [{self._id}]>'


class Singleton(Entity):
    @classmethod
    def get_id(cls, **kwargs):
        return 0
