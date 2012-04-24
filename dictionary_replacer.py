#coding:utf-8

"""
    Create a method that takes a string and a dictionary, and replaces 
    every key in the dictionary pre and suffixed with a dollar sign, 
    with the corresponding value from the Dictionary.

    Test Cases
    ----------

    input : "", dict empty
    output: ""

    input : "$temp$", dict ["temp", "temporary"]
    output: "temporary"

    input : "$temp$ here comes the name $name$", dict ["temp", "temporary"] ["name", "John Doe"]
    output : "temporary here comes the name John Doe"

"""

import unittest

def dictionary_replacer(input_str, dictionary):
    if type(dictionary) is type({}):
        for key, value in dictionary.iteritems():
            lookup = "$%s$" % key
            if lookup in input_str:
                input_str = input_str.replace(lookup, value)

    return input_str

class DictionaryReplacerTest(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(
            ""
            , dictionary_replacer("", {})
        ) 
    def test_simple_dict(self):
        self.assertEqual(
            "temporary"
            , dictionary_replacer("$temp$", {"temp":"temporary"})
        )
    def test_complex_dict(self):
        self.assertEqual(
            "temporary here comes the name John Doe"
            , dictionary_replacer("$temp$ here comes the name $name$", {"temp" : "temporary", "name" : "John Doe"})
        )

if __name__ == '__main__':
    unittest.main()
