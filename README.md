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
socat TCP-LISTEN:2375,reuseaddr,fork UNIX-CONNECT:/var/run/docker.sock &
docker-compose build --no-cache && docker-compose --project-name hl7v2 up -d && docker image prune -fa
```

or pull the image from Docker Hub:

```bash
docker pull drbenjamin/hl7v2:v1 && docker stop HL7v2 && docker rm HL7v2 && docker run --name HL7v2 --detach -p 8501:8501 drbenjamin/hl7v2:v1
```

## Automated system setup with Ansible

To run the Ansible playbook on MacOS use the following command:

```bash
xcode-select --install
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
```

Create a inventory file:

```yml
all:
  vars:
    ansible_user: <username>
  hosts:
    computer1:
      ansible_host: <ip.address>
      ansible_ssh_private_key_file: ~/.ssh/<keyfile>
```

Finally run the playbook:

```bash 
ansible-playbook -i ~/.ansible/inventory.yml ansible_osx.yml --ask-become-pass
```
