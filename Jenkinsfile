pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('github-creds_odc')
        IMAGE_BACKEND = 'mormbathie/odc_backend'
        IMAGE_FRONTEND = 'mormbathie/odc_frontend'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'Main', url: 'https://github.com/mormbathie/projetfilerougedock.git'

            }
        }

        stage('Tests Backend') {
            steps {
                dir('backend') {
                    sh 'pip install -r requirements.txt'
                    echo 'Pas encore de tests à exécuter.'
                }
            }
        }

        stage('Build Frontend (React)') {
            steps {
                dir('frontend') {
                    sh 'npm install'
                    sh 'npm run build'
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker build -t $IMAGE_BACKEND ./backend'
                sh 'docker build -t $IMAGE_FRONTEND ./frontend'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: "$DOCKER_HUB_CREDENTIALS", url: ""]) {
                    sh 'docker push $IMAGE_BACKEND'
                    sh 'docker push $IMAGE_FRONTEND'
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                // Tu dois être dans le dossier où se trouve docker-compose.yml
                sh 'docker-compose down || true'
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        success {
            mail to: 'mormbathie98@gmail.com',
                 subject: "✔️ Build Success - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Le pipeline Jenkins a réussi avec succès ! 🎉"
        }
        failure {
            mail to: 'mormbathie98@gmail.com',
                 subject: "❌ Build Failed - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Le pipeline Jenkins a échoué. Va checker les logs dans Jenkins 😢"
        }
    }
}
