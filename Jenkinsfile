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
         stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh '''
                        . venv/bin/activate
                        sonar-scanner
                    '''
                }
            }
        }

    
        stage('Deploy') {
            steps {
                sh '''
                pkill -f gunicorn || true

                nohup ./venv/bin/gunicorn Naturepro.wsgi:application \
                --bind 0.0.0.0:9090 > gunicorn.log 2>&1 &
                '''
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