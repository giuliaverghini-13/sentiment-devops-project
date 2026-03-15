pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'python -m pip install --upgrade pip'
                sh 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                echo 'Running automated tests...'
                sh 'pytest'
            }
        }

        stage('Build Docker image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t sentiment-api -f deployment/Dockerfile .'
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                echo 'Deploying application stack...'
                sh 'docker compose -f deployment/docker-compose.yml up -d --build'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}