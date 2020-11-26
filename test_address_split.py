from unittest import TestCase
from address_split import *


class TestAddress(TestCase):

    def test_streetname_number(self):
        address1 = "Midscheeps 1"
        street_addr, house_nr_str = address_split(address1)
        assert street_addr == 'Midscheeps', "Should be Midscheeps"
        assert house_nr_str == '1', "Should be 1"

    def test_null(self):
        address1 = ""
        street_addr, house_nr_str = address_split(address1)
        assert street_addr == '', "Should be empty"
        assert house_nr_str == "none", "Should be None"
