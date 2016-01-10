from unittest import TestCase

from const_choice import Consts, C


class ConstsTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super(ConstsTests, cls).setUpClass()

    def setUp(self):
        pass

    def test_interface(self):
        consts = Consts(
            CONST_A=C(
                id=101,
                label='label_a'
            ),
            CONST_B=C(
                id=102,
                label='label_b'
            ),
            CONST_C=C(
                id=100,
                label='label_c'
            )
        )
        self.assertEqual(consts.CONST_A, 101)
        self.assertEqual(consts.CONST_B, 102)
        self.assertEqual(consts.CONST_C, 100)
        self.assertEqual(consts['CONST_A'], 101)
        self.assertEqual(consts['CONST_B'], 102)
        self.assertEqual(consts['CONST_C'], 100)
        self.assertEqual(consts.const_a.get_name(), 'CONST_A')
        self.assertEqual(consts.const_b.get_name(), 'CONST_B')
        self.assertEqual(consts.const_c.get_name(), 'CONST_C')
        self.assertEqual(consts['const_a'].get_name(), 'CONST_A')
        self.assertEqual(consts['const_b'].get_name(), 'CONST_B')
        self.assertEqual(consts['const_c'].get_name(), 'CONST_C')
        self.assertEqual(consts.get_choices(), ((101, 'label_a'), (102, 'label_b'), (100, 'label_c')))
        self.assertEqual(consts.get_consts(), (consts.const_a, consts.const_b, consts.const_c))
        self.assertEqual(consts.get_consts_names(), ('CONST_A', 'CONST_B', 'CONST_C'))
        self.assertEqual(consts.get_by_id(consts.CONST_A), consts.const_a)
        self.assertEqual(consts.get_by_id(consts.CONST_B), consts.const_b)
        self.assertEqual(consts.get_by_id(consts.CONST_C), consts.const_c)
        self.assertEqual(consts.get_by_name('CONST_A'), consts.CONST_A)
        self.assertEqual(consts.get_by_name('const_A'), consts.const_a)

    def test_choices_getter(self):

        consts = Consts(
            CONST_A=C(
                id=101,
                label_another='label_a'
            ),
            CONST_B=C(
                id=102,
                label_another='label_b'
            ),
            CONST_C=C(
                id=100,
                label_another='label_c'
            ),
            choice=lambda obj: obj.label_another
        )
        self.assertEqual(consts.CONST_A, 101)
        self.assertEqual(consts.CONST_B, 102)
        self.assertEqual(consts.CONST_C, 100)
        self.assertEqual(consts.get_choices(), ((101, 'label_a'), (102, 'label_b'), (100, 'label_c')))

    def test_auto_setting_ids(self):
        consts = Consts(
            CONST_A=C(
                label='label_a'
            ),
            CONST_B=C(
                label='label_b'
            ),
            CONST_C=C(
                label='label_c'
            )
        )
        self.assertEqual(consts.CONST_A, 1)
        self.assertEqual(consts.CONST_B, 2)
        self.assertEqual(consts.CONST_C, 3)

    def test_zero_id(self):
        consts = Consts(
            CONST_A=C(
                id=0,
                label='label_a'
            ),
            CONST_B=C(
                id=1,
                label='label_b'
            ),
            CONST_C=C(
                id=2,
                label='label_c'
            )
        )
        self.assertEqual(consts.CONST_A, 0)
        self.assertEqual(consts.CONST_B, 1)
        self.assertEqual(consts.CONST_C, 2)

    def test_incorrect_some_with_id_some_without(self):
        create = lambda: Consts(
            CONST_A=C(
                label='label_a'
            ),
            CONST_B=C(
                id=101,
                label='label_b'
            ),
            CONST_C=C(
                id=102,
                label='label_c'
            )
        )

        self.assertRaises(ValueError, create)

    def test_different_const_inits(self):
        consts = Consts(
            CONST_A=C(
                id=101,
                label='label_a'
            ),
            CONST_B=C(
                102,
                label='label_b'
            ),
            CONST_C=C({
                'id': 100,
                'label': 'label_c'
            })
        )
        self.assertEqual(consts.CONST_A, 101)
        self.assertEqual(consts.CONST_B, 102)
        self.assertEqual(consts.CONST_C, 100)

    def test_accept_only_uppercase(self):
        create = lambda: Consts(
            const_A=C(
                id=101,
                label='label_a'
            ),
            CONST_B=C(
                id=102,
                label='label_b'
            ),
            CONST_C=C(
                id=100,
                label='label_c'
            )
        )
        self.assertRaises(ValueError, create)

    def test_incorrect_duplicate_id(self):
        create = lambda: Consts(
            CONST_A=C(
                id=101,
                label='label_a'
            ),
            CONST_B=C(
                id=102,
                label='label_b'
            ),
            CONST_C=C(
                id=101,
                label='label_c'
            )
        )
        self.assertRaises(ValueError, create)

    def test_get_by_id_args(self):
        consts = Consts(
            CONST_A=C(
                id=101,
                label_another='label_a'
            ),
            CONST_B=C(
                id=102,
                label_another='label_b'
            ),
            CONST_C=C(
                id=100,
                label_another='label_c'
            ),
            choice=lambda obj: obj.label_another
        )

        # correct ids
        self.assertEqual(consts.const_a, consts.get_by_id(101))
        self.assertEqual(consts.const_a, consts.get_by_id('101'))
        # incorrect id
        self.assertEqual(None, consts.get_by_id(None))
        # different non existing ids
        self.assertEqual(None, consts.get_by_id('non_existing_string_id'))
        self.assertEqual(None, consts.get_by_id('99999'))
        self.assertEqual(None, consts.get_by_id(99999))

