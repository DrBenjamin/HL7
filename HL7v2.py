import streamlit as st
from hl7apy.parser import parse_message
from hl7apy.core import Group, Segment

# Function to parse HL7 message
def parse_hl7_message(message):
    return parse_message(message)

# Opening sample document
file = st.file_uploader("Upload HL7 message", type=['hl7', 'txt'])
try:
  message = file.read().decode('utf-8')
  msg = parse_hl7_message(message)
  
  # Printing the message
  st.header("HL7 Message parser")
  st.subheader("HL7 Message (cleaned):")
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
  #st.write(e)
