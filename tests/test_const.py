from unittest import TestCase

from const_choice import Const


class ConstTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super(ConstTests, cls).setUpClass()

    def setUp(self):
        pass

    def test_only_kwargs(self):
        """
        Test initializing with kwargs and additionally full interface.
        """
        c = Const(
            id=99,
            label='label_value',
            other_data='other_data_value'
        )
        self.assertEqual(c.id, 99)
        self.assertEqual(c.get_id(), 99)
        self.assertEqual(c.get_name(), 'UNKNOWN_NAME')
        self.assertEqual(c.label, 'label_value')
        self.assertEqual(c['label'], 'label_value')
        self.assertEqual(c.other_data, 'other_data_value')
        self.assertEqual(c['other_data'], 'other_data_value')
        self.assertEqual(set(c.keys()), {'label', 'other_data'})
        self.assertEqual(set(c.get_attrs()), {'label', 'other_data'})
        self.assertEqual(set(c.items()), {('label', 'label_value'), ('other_data', 'other_data_value')})
        self.assertEqual(set(c.values()), {'label_value', 'other_data_value'})

    def test_id_arg_and_kwargs(self):
        c = Const(
            99,
            label='label_value',
            other_data='other_data_value'
        )
        self.assertEqual(c.id, 99)
        self.assertEqual(set(c.items()), {('label', 'label_value'), ('other_data', 'other_data_value')})

    def test_only_dict_arg(self):
        c = Const({
            'id': 99,
            'label': 'label_value',
            'other_data': 'other_data_value'
        })
        self.assertEqual(c.id, 99)
        self.assertEqual(set(c.items()), {('label', 'label_value'), ('other_data', 'other_data_value')})

    def test_id_arg_and_dict_arg(self):
        c = Const(
            99,
            {'label': 'label_value',
             'other_data': 'other_data_value'})
        self.assertEqual(c.id, 99)
        self.assertEqual(set(c.items()), {('label', 'label_value'), ('other_data', 'other_data_value')})

    def test_zero_id(self):
        c = Const(
            id=0,
            label='label_value',
            other_data='other_data_value'
        )
        self.assertEqual(c.id, 0)
        self.assertEqual(set(c.items()), {('label', 'label_value'), ('other_data', 'other_data_value')})

    def test_set_name(self):
        c = Const(0)
        self.assertEqual(c.get_name(), 'UNKNOWN_NAME')
        c._set_name('CONST_NAME')
        self.assertEqual(c.get_name(), 'CONST_NAME')

    def test_dir(self):
        self.assertEqual(set(dir(Const(0)) + ['my_attr', 'my_second_attr']),
                         set(dir(Const(0, my_attr='value', my_second_attr='value'))))
