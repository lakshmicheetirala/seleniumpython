import unittest
from package1.tc_logintest import LoginTest
from package1.tc_signup import SignupTest

from package2.tc_paymenttest import PaymentTest
from package2.tc_paymentreturnstest import PaymentReturnsTest

# Get all Tests from packages

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# Creating Test suites

sanitytestsuite = unittest.TestSuite([tc1, tc2])  # Sanity Test Suite
functionaltestsuite = unittest.TestSuite([tc3, tc4])  # Funtional Test suite
mastertestsuite = unittest.TestSuite([tc1, tc2, tc3, tc4])  # master Test suite

unittest.TextTestRunner(verbosity=2).run(mastertestsuite)
