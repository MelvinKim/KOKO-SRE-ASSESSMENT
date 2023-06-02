pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('f3f94151-2740-4a88-a0c8-3076c49ad1c4')
        AWS_ACCESS_KEY_ID     = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
        DOCKER_IMAGE = "melvinkimathi/koko-sre-assessment:${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout repository') {
            steps {
               checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/MelvinKim/KOKO-SRE-ASSESSMENT.git']])
            }
        }
        stage('Run tests') {
            steps {
                sh 'python3 test_app.py'
            }
        }
        stage('Build docker image') {
            steps {
                sh 'docker build --platform=linux/amd64 -t {DOCKER_IMAGE} .'
            }
        }
        stage('Push docker image to docker image to docker hub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push {DOCKER_IMAGE} .'  
            }
        }
        stage('Provision EC2 Instance and Deploy App') {
            steps {
                //to suppress warnings when you execute playbook    
                // sh "pip install --upgrade requests==2.20.1"
                sh "ansible-playbook --syntax-check deploy-to-EC2.yml"
                sh "ansible-playbook deploy-to-EC2.yml --extra-vars 'docker_image=${env.DOCKER_IMAGE}'"
            }
        }
    }
}
