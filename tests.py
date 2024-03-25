# tests.py
import unittest
import hl7apy
from HL7v2 import parse_hl7_message

class SimpleTest(unittest.TestCase):
    def test_parse_hl7_message(self):
        self.assertTrue(isinstance(parse_hl7_message(r"""MSH|^~\&|HL7Soup|Instance1|HL7Soup|Instance2|200808181126|SECURITY|ADT^A01^ADT_A01|MSG00001|P|2.5"""), hl7apy.core.Message))

    def test2_parse_hl7_message(self):
        self.assertEqual(parse_hl7_message(r"""MSH|^~\&|HL7Soup|Instance1|HL7Soup|Instance2|200808181126|SECURITY|ADT^A01^ADT_A01|MSG00001|P|2.5""").children[0].children[2].value, "HL7Soup")
        
    def test3_parse_hl7_message(self):
        self.assertEqual(parse_hl7_message(r"""MSH|^~\&|HL7Soup|Instance1|HL7Soup|Instance2|200808181126|SECURITY|ADT^A01^ADT_A01|MSG00001|P|2.5""").children[0].children[11].value, "2.5")
