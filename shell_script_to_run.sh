#!/bin/zsh
killall python
/Users/benjamin.gross1/miniconda3/bin/python -m pytest --junitxml results.xml tests.py &
/Users/benjamin.gross1/miniconda3/bin/python -m streamlit run HL7v2.py &
