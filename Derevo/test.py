import unittest
import Model

class TestModel(unittest.TestCase):
    

    def test_updateAlbums(self):
        self._model = Model.Model()
        self._model.updateAlbums(3, 'God of War')
        test = self._model.getAlbumsSQL()
        self.assertIn(['God of War', 3], test)



if __name__ == '__main__':
    unittest.main()