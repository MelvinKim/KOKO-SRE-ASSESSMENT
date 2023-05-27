pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }

    stages {
        stage('Checkout repository') {
            steps {
                git 'https://github.com/MelvinKim/KOKO-SRE-ASSESSMENT.git'
            }
        }
        stage('Run tests') {
            steps {
                sh 'python3 test_app.py'
            }
        }
        stage('Build docker image') {
            steps {
                sh 'docker build -t melvinkimathi/koko-sre-assessment:v1 .'
            }
        }
        stage('Push docker image to docker image to docker hub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push melvinkimathi/koko-sre-assessment:v1'
            }
        }
        stage('Create an EC2 instance - Ansible') {
            steps {
                
            }
        }
        stage('Deploy app - using Docker') {
            steps {
                echo 'spin up a docker container'
            }
        }
    }

    post {
		always {
			sh 'docker logout'
		}
	}
}
