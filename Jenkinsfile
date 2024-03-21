pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/DrBenjamin/HL7']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/DrBenjamin/HL7'
                sh 'python -m streamlit run HL7v2.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m pytest --junitxml results.xml tests.py'
            }
        }
    }
}