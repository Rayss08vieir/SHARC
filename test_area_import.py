# test_area_import.py

import unittest

class TestAreaImport(unittest.TestCase):
    def test_import(self):
        try:
            import area
            self.assertTrue(True, "Módulo 'area' importado com sucesso!")
        except ImportError:
            self.fail("Erro ao importar o módulo 'area'")

if __name__ == '__main__':
    unittest.main()
