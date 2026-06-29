pipeline {
    agent { label 'agent3' }
     environment {
        JFROG_URL = 'http://13.233.233.45:8082/artifactory/django-artifacts'
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }


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
                    sh "${tool('sonar-scanner')}/bin/sonar-scanner"
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
                        tar -czf /tmp/app-${BUILD_NUMBER}.tar.gz \
                            --exclude=venv \
                            --exclude=.git \
                            --exclude=.scannerwork \
                            --exclude=*.tar.gz \
                            .

                        curl -u $JFROG_USER:$JFROG_TOKEN \
                            -T /tmp/app-${BUILD_NUMBER}.tar.gz \
                            "$JFROG_URL/app-${BUILD_NUMBER}.tar.gz"

                        rm -f /tmp/app-${BUILD_NUMBER}.tar.gz
                    '''
                }
            }
        }
    
        stage('Deploy') {
            steps {
                sh '''

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