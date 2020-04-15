import unittest
from my_sum import my_sum

class test_my_sum(unittest.TestCase):
    def test_list(self):
        x = [1,2,3,4,5]
        result = my_sum(x)

        self.assertEqual(result, 15)

    def test_tuple(self):
        x = (1,2,3,4,5)
        result = my_sum(x)
        
        self.assertEqual(result, 15)
    
    def test_error(self):
        x = 1
        #self.assertEqual(result, 1)
        with self.assertRaises(TypeError):
            result = my_sum(x)



if __name__ == '__main__':
    unittest.main()