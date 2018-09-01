import unittest
from bissexto import bissexto

class TestBissexto(unittest.TestCase):
    def test_ebissexto_verdadeiro(self):
        self.assertEqual(True, bissexto(4), 'ano: {}'.format(1600))
        self.assertEqual(True,bissexto(1600),'ano: {}'.format(1600))
        self.assertEqual(True,bissexto(1732),'ano: {}'.format(1732))
        self.assertEqual(True, bissexto(1888),'ano: {}'.format(1888))
        self.assertEqual(True, bissexto(1944),'ano: {}'.format(1944))

    def test_ebissexto_falso(self):
        self.assertEqual(False, bissexto(1000), 'ano: {}'.format(1000))
        self.assertEqual(False, bissexto(1742),'ano: {}'.format(1742))
        self.assertEqual(False, bissexto(1889),'ano: {}'.format(1889))
        self.assertEqual(False, bissexto(1951),'ano: {}'.format(1951))
        self.assertEqual(False, bissexto(2011),'ano: {}'.format(2011))

if __name__=='__main__':
    unittest.main()