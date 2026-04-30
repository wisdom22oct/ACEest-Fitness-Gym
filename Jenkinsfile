pipeline {
    agent any

    tools {
        python 'Python3'   // Make sure Jenkins has Python installed
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/wisdom22oct/ACEest-Fitness-Gym.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest -v --junitxml=results.xml'
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }

        stage('SonarQube Analysis') {
            environment {
                SONARQUBE = credentials('sonarqube-token') // configure in Jenkins
            }
            steps {
                sh '''
                sonar-scanner \
                  -Dsonar.projectKey=ACEESTAPP \
                  -Dsonar.sources=. \
                  -Dsonar.host.url=http://localhost:9000 \
                  -Dsonar.login=$SONARQUBE
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t aceestapp:latest .'
            }
        }

        stage('Push to DockerHub') {
            environment {
                DOCKERHUB = credentials('dockerhub-creds')
            }
            steps {
                sh '''
                echo $DOCKERHUB_PSW | docker login -u $DOCKERHUB_USR --password-stdin
                docker tag aceestapp:latest yourdockerhub/aceestapp:latest
                docker push yourdockerhub/aceestapp:latest
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}
