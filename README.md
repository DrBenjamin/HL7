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

Build and run docker container:

```bash
# Build and run the container
docker-compose build --no-cache && docker-compose --project-name hl7v2 up -d && docker image prune -fa
```

or pull the image from Docker Hub:

```bash
# Pull and run the container
docker pull drbenjamin/hl7v2:v1 && docker stop HL7v2 && docker rm HL7v2 && docker run --name HL7v2 --detach -p 8501:8501 drbenjamin/hl7v2:v1
```

### nextgen Connect

Pull and run docker container:

```bash
# Pull and run the container
docker pull nextgenhealthcare/connect && docker run --name connect -d -p 8443:8443 -p 20000:20000 nextgenhealthcare/connect
```