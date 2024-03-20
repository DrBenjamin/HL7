import streamlit as st
from hl7apy.parser import parse_message
from hl7apy.core import Group, Segment

def parse_hl7_message(message):
    return parse_message(message)

with open('sample_message.txt', 'r') as file:
    message = file.read()
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
 