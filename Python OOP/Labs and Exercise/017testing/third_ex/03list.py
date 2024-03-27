# from third_ex.code import IntegerList
from unittest import TestCase, main



class TestCat(TestCase):
    def setUp(self):
        self.int_list = IntegerList(5.5, 1,2,3,"deniz")

    def test_correct_init_ignores_non_int_values(self):
        self.assertEqual([1, 2, 3], self.int_list.get_data())

    def test_add_element_if_element_is_non_int_raise_value_error(self):
            with self.assertRaises(ValueError) as ve:
                self.int_list.add(5.5)

            self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_element_if_element_is_integer(self):
        expected_result = self.int_list.get_data() + [4]

        self.int_list.add(4)

        self.assertEqual(expected_result, self.int_list.get_data())

    def test_remove_index_if_index_is_invalid_raise_value_error(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.remove_index(1000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_with_correct_index(self):
        expected_result = [1, 2]

        self.int_list.remove_index(2)

        self.assertEqual(expected_result, self.int_list.get_data())

    def test_get_element_when_index_is_ot_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.get(1000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_when_index_is_in_range(self):
        expected_result = self.int_list.get(1)

        self.assertEqual(expected_result, self.int_list.get(1))

    def test_insert_element_when_index_is_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.insert(1000, 3)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_element_when_element_is_not_int(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.insert(1, 3.4)

        self.assertEqual("Element is not Integer", str(ve.exception))


    def test_insert_integer_on_valid_index(self):
        expected_list = self.int_list.get_data().copy()

        expected_list.insert(1, 5)
        self.int_list.insert(1, 5)

        self.assertEqual(expected_list, self.int_list.get_data())

    def test_get_bigger(self):
        result = self.int_list.get_biggest()
        self.assertEqual(3, result)

    def test_get_index(self):
        result = self.int_list.get_index(2)
        self.assertEqual(1, result)


if __name__ == "__main__":
    main()
