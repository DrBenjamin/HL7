# HL7
All HL7 standards

## Usage

```bash
python -m pip install --upgrade -r requirements.txt
python -m streamlit run HL7v2.py
python -m pytest --junitxml results.xml tests.py
```

## Docker Cloud for Jenkins

Open port for Jenkins on Docker for Mac.

```bash
socat TCP-LISTEN:2375,reuseaddr,fork UNIX-CONNECT:/var/run/docker.sock
```