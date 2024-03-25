# HL7
All HL7 standards.

## Usage

To run the app locally use the following commands:

```bash
python -m pip install --upgrade -r requirements.txt
python -m streamlit run HL7v2.py
python -m pytest --junitxml results.xml tests.py
```

## Docker

Build und run docker container:

```bash
socat TCP-LISTEN:2375,reuseaddr,fork UNIX-CONNECT:/var/run/docker.sock
docker-compose build --no-cache && docker-compose --project-name hl7v2 up -d && docker image prune -fa
```
