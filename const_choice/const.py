from types import NoneType

__all__ = ('Const', 'C')


class Const(object):
    creation_counter = 0

    def __init__(self, id_or_attrs_dict=None, attrs_dict=None, **attrs_kwargs):
        assert isinstance(id_or_attrs_dict, (int, dict, NoneType)), \
            'First arg (if given) should be id integer or attributes dict: "%s."' % id_or_attrs_dict
        assert isinstance(attrs_dict, (dict, NoneType)), \
            'Second arg (if given) should be attributes dict: "%s."' % attrs_dict
        assert not (isinstance(id_or_attrs_dict, dict) and isinstance(attrs_dict, dict)), \
            'If first arg is attributes dict, second should be omitted.'

        self.creation_counter = C.creation_counter
        C.creation_counter += 1

        self.id = None
        self.cname = None

        # retrieve id and attrs
        if id_or_attrs_dict is None:
            self.id = attrs_kwargs.pop('id', None)
        elif isinstance(id_or_attrs_dict, dict):
            self.id = id_or_attrs_dict.pop('id', None)
            attrs_kwargs.update(id_or_attrs_dict)
        else:
            self.id = id_or_attrs_dict
            if attrs_dict:
                attrs_kwargs.update(attrs_dict)
        self.attrs = attrs_kwargs

    def _set_name(self, name):
        self.cname = name

    def get_name(self):
        return self.cname or 'UNKNOWN_NAME'

    def get_id(self):
        return self.id

    def get_attrs(self):
        return self.keys()

    def keys(self):
        return self.attrs.keys()

    def values(self):
        return self.attrs.values()

    def items(self):
        return self.attrs.items()

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError("this Const object has not attribute '%s'" % item)

    def __getitem__(self, item):
        return self.attrs[item]

    def __repr__(self):
        return '<%s: %s %s>' % (self.get_name(), self.id, str(self.attrs))

    def __dir__(self):
        return dir(super(Const, self)) + list(self.keys())

C = Const
