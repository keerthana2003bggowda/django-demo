pipeline {
    agent { label 'agent3' }

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
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            
            }
        }
        stage('SonarCloud Report') {
            steps {
                withSonarQubeEnv('sonarcloud') {       
                    sh '''
                        sonar-scanner \
                          -Dsonar.projectKey=keerthana2003bggowda_django-demo \
                          -Dsonar.organization=keerthana2003bggowda \
                          -Dsonar.sources=. \
                          -Dsonar.exclusions=venv/**,**/__pycache__/**,**/*.pyc
                    '''
                }
            }
        }

    
        stage('Deploy') {
            steps {
                sh 'nohup gunicorn Naturepro.wsgi:application --bind 0.0.0.0:9090 '
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