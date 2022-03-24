#Importing Libraries
import unittest
from unittest.mock import *
from src.general_example import GeneralExample
#Initializing class object
ge = GeneralExample()

class Test_General(unittest.TestCase):
    
    #first test
    def test_flatten_dictionary(self):
        self.assertEqual(ge.flatten_dictionary({'r': [1,2,3], 'd' : [5,6,8], 'p': [9,2,1]}), [1, 2, 3, 5, 6, 8, 9])
       
    #Secong test
    def test_load_employee_rec_from_database(self):
        self.assertEqual(ge.load_employee_rec_from_database(),['emp001', 'Sam', '100000'])
        
    #Test with mock on load_employees_rec_from_database() method    
    def test_fetch_emp_details(self):
        with patch.object(GeneralExample, 'load_employee_rec_from_database', return_value = ['emp002', 'Jane', '9856325']):
            assert ge.fetch_emp_details() == {'empId': 'emp002', 'empName': 'Jane', 'empSalary': '9856325'}
if __name__ == "__main__":
    unittest.main()

