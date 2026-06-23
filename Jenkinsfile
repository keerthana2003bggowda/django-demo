pipeline {
    agent { label 'agent3' }
     environment {
        JFROG_CREDS = credentials('artifactory-creds')
        JFROG_URL = 'http://13.203.219.26:8082/artifactory/django-artifacts'
    }

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
        
        stage('Publish to JFrog') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'artifactory-creds',
                    usernameVariable: 'JFROG_USER',
                    passwordVariable: 'JFROG_TOKEN'
                )]) {
                    sh '''
                        tar --exclude=venv \
                        --exclude=.git \
                        --exclude=__pycache__ \
                        --exclude=*.pyc \
                        --exclude=*.tar.gz
                        -czf django-demo-${BUILD_NUMBER}.tar.gz .

                    curl -u $JFROG_USER:$JFROG_TOKEN \
                     -T django-demo-${BUILD_NUMBER}.tar.gz \
                     "http://13.203.219.26:8082/artifactory/django-artifacts/django-demo-${BUILD_NUMBER}.tar.gz"
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