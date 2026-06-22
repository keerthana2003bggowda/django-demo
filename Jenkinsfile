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
        stage('SonarQube Report') {
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh '''
                        export SONAR_SCANNER_OPTS="-Xmx1024m"
                        sonar-scanner \
                          -Dsonar.projectKey=django-demo \
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