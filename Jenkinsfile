pipeline {
    agent { label 'agent3 }

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
                python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('sonarqubereport'){
            steps{
                withSonarQubeEnv('sonarcloud') {
                    sh 'mvn sonar:sonar'
                }
            }
        }


        stage('Deploy') {
            steps {
                sh 'nohup gunicor Naturepro.wsgi:application --bind 0.0.0.0:9090 > app.log 2>&1 &'
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