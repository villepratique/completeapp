from django.test import TestCase
from generator.helper import generatePDF, loadFixtures


class AnimalTestCase(TestCase):
    def setUp(self):
        pass

    def test_can_generatePDF(self):
        data = loadFixtures()
        item = data[1]

        generatePDF(item)
        self.assertNotEqual(item.city, "")