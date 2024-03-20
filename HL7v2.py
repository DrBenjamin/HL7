import streamlit as st
import hl7apy
from hl7apy.parser import parse_message
from hl7apy.core import Group, Segment

# Function to parse HL7 message
def parse_hl7_message(message):
    return parse_message(message)

# Opening sample document
with open('sample_message.hl7', 'r') as file:
    message = file.read()
msg = parse_hl7_message(message)

# Testing
assert isinstance(parse_hl7_message("MSH|^~\&|HL7Soup|Instance1|HL7Soup|Instance2|200808181126|SECURITY|ADT^A01^ADT_A01|MSG00001|P|2.5"), hl7apy.core.Message)

# Printing the message
st.header("HL7 Message parser")
st.subheader("Message:")
for segment in msg.children:
    if isinstance(segment, Segment):
        for attribute in segment.children:
            #print(attribute, attribute.value)
            st.write(attribute.value)
    if isinstance(segment, Group):
        for group in segment.children:
            for group_segment in group.children:
                for attribute in group_segment.children:
                    #print(attribute, attribute.value)
                    st.write(attribute.value)