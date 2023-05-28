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
                sh 'docker build -t melvinkimathi/koko-sre-assessment:v1.1.1 .'
            }
        }
        stage('Push docker image to docker image to docker hub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker build -t melvinkimathi/koko-sre-assessment:v1.1.1 .'  
            }
        }
        stage('Provision EC2 Instance') {
            steps {
                script{
                    dir("terraform") {
                    echo "provisioning EC2 Instance ......"
                    sh 'cd terraform/ ; terraform init'
                    sh "cd terraform/ ; terraform plan -out tfplan"
                    sh 'cd terraform/ ; terraform show -no-color tfplan > tfplan.txt'
                    def plan = readFile 'terraform/tfplan.txt'
                    input message: "Do you want to apply the plan?",
                    parameters: [text(name: 'Plan', description: 'Please review the plan', defaultValue: plan)]
                    sh "cd terraform/ ; terraform apply -input=false tfplan"
                    }
                }
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
