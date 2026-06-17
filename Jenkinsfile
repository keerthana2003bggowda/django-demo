pipeline {
    agent { label 'agent1' }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-pat',
                    url: 'https://github.com/keerthana2003bggowda/django-demo.git'
            }
        }

        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('sonarqubereport') {
            steps {
                withSonarQubeEnv('sonarcloud') {
                    sh 'sonar-scanner'
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'nohup gunicorn myproject.wsgi:application --bind 0.0.0.0:9090 > app.log 2>&1 &'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}