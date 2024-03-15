from tests.test_data_handler import TestDataHandler
import unittest, json


# dh = DataHandler(get_data_handler())

loader = unittest.TestLoader()
suite = unittest.TestSuite()
# test = TestDataHandler(dh)
suite.addTest(loader.loadTestsFromTestCase(TestDataHandler))

runner = unittest.TextTestRunner()
runner.run(suite)
