import streamlit as st
import pandas as pd
import json
from hl7apy.parser import parse_message
from hl7apy.core import Group, Segment

# Function to parse HL7 message
def parse_hl7_message(message):
    return parse_message(message)

# Opening sample document
file = st.file_uploader("Upload HL7 message", type=['hl7', 'txt'])
try:
  message = file.read().decode('utf-8').replace('\n', '\r')
  
  # Parsing the message
  st.subheader("HL7 Message (parsed):")
  msg = parse_hl7_message(message)
  msg_json = []
  for segment in msg.children:
      if isinstance(segment, Segment):
          for attribute in segment.children:
              print(attribute.name, attribute.value)
              st.write(f"{attribute.name}: {attribute.value}")
              msg_json.append({attribute.name: attribute.value})
      if isinstance(segment, Group):
          for group in segment.children:
              for group_segment in group.children:
                  for attribute in group_segment.children:
                      print(attribute.name, attribute.value)
                      st.write(f"{attribute.name}: {attribute.value}")
                      msg_json.append({attribute.name: attribute.value})
                      
except Exception as e:
  print(e)

# Saving to JSON file
with open('output.json', 'w') as json_file:
    json.dump(msg_json, json_file)
