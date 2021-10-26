from unittest import TestCase

import numpy

from report import refactor_sex, refactor_dict_location, refactor_date


class test_refactor_sex(TestCase):
    def test_refactor_sex_female(self):
        female_digit = 1
        self.assertEqual(refactor_sex(female_digit), 'Female')

    def test_refactor_sex_male(self):
        male_digit = 2
        self.assertEqual(refactor_sex(male_digit), 'Male')

    def test_refactor_sex_float(self):
        male_float = 2.0
        self.assertRaises(ValueError, refactor_sex, male_float)

    def test_refactor_sex_list(self):
        male_list = [2]
        self.assertRaises(ValueError, refactor_sex, male_list)

    def test_refactor_sex_dict(self):
        male_dict = {'Male': 2}
        self.assertRaises(ValueError, refactor_sex, male_dict)

    def test_refactor_sex_str(self):
        male_str = '2'
        self.assertRaises(ValueError, refactor_sex, male_str)

    def test_refactor_sex_nan(self):
        nan = numpy.NAN
        self.assertRaises(ValueError, refactor_sex, nan)


class test_refactor_dict_location(TestCase):
    def test_refactor_location_expected_dict(self):
        location_dict = {'id': 1, 'title': 'Moscow'}
        self.assertEqual(refactor_dict_location(location_dict), 'Moscow')

    def test_refactor_location_nan(self):
        nan = numpy.NAN
        self.assertEqual(refactor_dict_location(nan), 'Unknown')

    def test_refactor_location_unexpected_dict(self):
        another_dict = {'animal': 'dog'}
        self.assertEqual(refactor_dict_location(another_dict), 'Unknown')

    def test_refactor_location_empty_dict(self):
        empty_dict = {}
        self.assertEqual(refactor_dict_location(empty_dict), 'Unknown')

    def test_refactor_location_list(self):
        location_list = ['title']
        self.assertRaises(ValueError, refactor_dict_location, location_list)

    def test_refactor_location_str(self):
        location_str = 'title: Moscow'
        self.assertRaises(ValueError, refactor_dict_location, location_str)


class test_refactor_date(TestCase):
    def test_refactor_date_expected(self):
        full_date = '12.12.1212'
        self.assertEqual(refactor_date(full_date), '1212-12-12')

    def test_refactor_date_shortd(self):
        short_date = '12.12'
        self.assertEqual(refactor_date(short_date), '0001-12-12')

    def test_refactor_date_unexpectedstr(self):
        unexpected_date = '12'
        self.assertRaises(ValueError, refactor_date, unexpected_date)

    def test_refactor_date_emptystr(self):
        empty_str = ''
        self.assertRaises(ValueError, refactor_date, empty_str)

    def test_refactor_date_nan(self):
        nan = numpy.NAN
        self.assertEqual(refactor_date(nan), '0001-01-01')

    def test_refactor_date_int(self):
        date_int = 12
        self.assertRaises(ValueError, refactor_date, date_int)

    def test_refactor_date_wday(self):
        wrong_day = '32.12.12'
        self.assertRaises(ValueError, refactor_date, wrong_day)

    def test_refactor_date_wmonth(self):
        wrong_month = '12.13.12'
        self.assertRaises(ValueError, refactor_date, wrong_month)

    def test_refactor_date_wyear(self):
        wrong_year = '12.12.a'
        self.assertRaises(ValueError, refactor_date, wrong_year)