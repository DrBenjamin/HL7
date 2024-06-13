import streamlit as st
import pandas as pd
import json
import re
from collections import namedtuple
from hl7apy.parser import parse_message
from hl7apy.core import Group, Segment

# Function to parse HL7 message
def parse_hl7_message(message):
    return parse_message(message)

# Funktion xy
def parse_message_func(hl7_msg):
    segments = re.findall(r'(\^[A-Z0-9]{3}\^\d{1,2})([^*]*)', hl7_msg)
    return [Segment(*segment) for segment in segments]

# Function to convert HL7v2 message to JSON format 
def convert_to_json(hl7_msg):
    msg = parse_message_func(hl7_msg)
    df = pd.DataFrame([[segment.name, segment.fields] for segment in msg])
    return df

# Opening sample document
file = st.file_uploader("Upload HL7 message", type=['hl7', 'txt'])
try:
  message = file.read().decode('utf-8')
  
  # Printing the message
  st.header("HL7 Message parser")
  st.subheader("HL7 Message (cleaned):")
  st.write(convert_to_json(message))
  
  # Parsing the message
  st.subheader("HL7 Message (parsed):")
  msg = parse_hl7_message(message)
  for segment in msg.children:
      if isinstance(segment, Segment):
          for attribute in segment.children:
              print(attribute, attribute.value)
              st.write(attribute.value)
      if isinstance(segment, Group):
          for group in segment.children:
              for group_segment in group.children:
                  for attribute in group_segment.children:
                      print(attribute, attribute.value)
                      st.write(attribute.value)
except Exception as e:
  print(e)
  st.write(e)
