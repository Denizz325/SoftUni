from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("name", "animal", "sound")

    def test_if_innit_is_correct_and_get_kingdom(self):
        self.assertEqual("name", self.mammal.name)
        self.assertEqual("animal", self.mammal.type)
        self.assertEqual("sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_if_sound_print_correct_message(self):
        self.assertEqual("name makes sound", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual("name is of type animal", self.mammal.info())



if __name__ == "__main__":
    main()