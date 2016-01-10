__all__ = ('Consts',)


class Consts(object):
    const_name_to_obj_name = staticmethod(lambda const_name: const_name.lower())
    obj_name_to_const_name = staticmethod(lambda const_name: const_name.upper())

    def __init__(self, choice=lambda x: x.label, **consts):
        """
        :param choice: optional function to be used for retrieving choice label
        :param consts: Const objects to be owned by this Consts instance
        :return:
        """
        # validate
        auto_ids = False

        no_ids = [True for c in consts.values() if c.id is None]
        if no_ids and len(no_ids) != len(consts):
            raise ValueError('All consts or none of them should have id')
        elif no_ids:
            auto_ids = True
        if len(consts) != len(tuple(key for key in consts.keys() if key.isupper())):
            raise ValueError('All consts names should be fully uppercase')
        if not auto_ids and \
                len(consts) != len(set(const_obj.id for const_obj in consts.values() if const_obj.id is not None)):
            raise ValueError('All consts ids should be unique')

        # sort
        consts_list = [(const_name, const_obj) for const_name, const_obj in consts.items()]
        consts_list.sort(key=lambda x: x[1].creation_counter)

        # own fields init
        self.consts_list = consts_list
        self.consts = consts
        self.choice_getter = choice
        self._choices = None
        self._consts_by_id = None

        # each const init completion
        for const_auto_id, const in enumerate(consts_list, start=1):
            const_name, const_obj = const
            # set const name
            const_obj._set_name(const_name)
            # if needed, set const id to auto value
            if const_obj.id is None:
                const_obj.id = const_auto_id

    def get_choices(self):
        """
        :return: tuple ( (id, label), (id, label), ...) generated using owned consts,
                 label is generated using choice constructor param
        """
        if self._choices is None:
            self._choices = tuple((obj.id, self.choice_getter(obj)) for name, obj in self.consts_list)
        return self._choices

    def get_consts(self):
        """
        :return: all consts obj owned by this Consts instance
        """
        return tuple(const_obj for const_name, const_obj in self.consts_list)

    def get_consts_names(self):
        """
        :return: all consts names owned by this Consts instance
        """
        return tuple(const_name for const_name, const_obj in self.consts_list)

    def get_by_id(self, const_id, default=None):
        """
        :param const_id: const integer id
        :return: whole Const object represented by this id
        """
        if self._consts_by_id is None:
            self._consts_by_id = {obj.id: obj for obj in self.consts.values()}

        try:
            return self._consts_by_id[const_id]
        except KeyError:
            try:
                const_id = int(const_id)
            except (TypeError, ValueError):
                return default
            return self._consts_by_id.get(const_id, default)

    def get_by_name(self, name, default=None):
        """
        :param name: const name - if lowercase Const, obj is returned; if uppercase, id is returned
        :return: whole Const object represented by this name or Const.id
        """
        const_name = self.obj_name_to_const_name(name)
        if const_name != name and const_name in self.consts:
            return self.consts[const_name]
        try:
            return self.consts[const_name].id
        except KeyError:
            raise AttributeError("this Consts object has not attribute '%s'" % name)

    def __getattr__(self, name):
        return self.get_by_name(name)

    def __getitem__(self, name):
        return self.get_by_name(name)

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.get_consts_names())
