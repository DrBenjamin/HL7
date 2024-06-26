import streamlit as st
from hl7apy.parser import parse_message
from hl7apy.core import Group, Segment

# Function to parse HL7 message
def parse_hl7_message(message):
    return parse_message(message)

# Opening sample document
with open('sample_message.hl7', 'r') as file:
    message = file.read()
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

#TODO: Add file uploader to upload HL7 messages
file = st.upload_file("Upload HL7 message", type=['hl7', 'txt'])
try:
  st.write(file.getvalue())
except Exception as e:
  print(e)
