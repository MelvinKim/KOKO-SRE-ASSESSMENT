pipeline {
    agent any
    parameters {
        booleanParam(name: 'autoApprove', defaultValue: false, description: 'Automatically run apply after generating plan?')
    } 
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        AWS_ACCESS_KEY_ID     = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
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
                sh 'docker build --platform=linux/amd64 -t melvinkimathi/koko-sre-assessment:v1.1.1 .'
            }
        }
        stage('Push docker image to docker image to docker hub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker build -t melvinkimathi/koko-sre-assessment:v1.1.1 .'  
            }
        }
        stage('Provision EC2 Instance and Deploy App') {
            steps {
                //to suppress warnings when you execute playbook    
                sh "pip install --upgrade requests==2.20.1"
                ansiblePlaybook playbook: 'deploy-to-EC2.yml'
            }
        }
    }

    post {
		always {
			sh 'docker logout'
		}
	}
}
