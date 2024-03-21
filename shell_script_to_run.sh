#!/bin/zsh
killall python
/Users/ben/miniconda3/bin/python -m streamlit run HL7v2.py &&
/Users/ben/miniconda3/bin/python -m pytest --junitxml results.xml tests.py
