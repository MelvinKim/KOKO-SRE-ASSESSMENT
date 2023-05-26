pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/MelvinKim/KOKO-SRE-ASSESSMENT.git']])
            }
        }
        stage('Run tests') {
            steps {
                sh 'python3 test_app.py'
            }
        }
    }
}
