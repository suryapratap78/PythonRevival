pipeline {
    agent any
    stages {

     stage('Debug Git') {
            steps {
                sh 'git --version'
                sh 'pwd'
                sh 'git ls-remote https://github.com/suryapratap78/PythonRevival.git'
            }
        }
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/suryapratap78/PythonRevival.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pwd'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python scratch_fw_pytest/validate_standalone.py'
            }
        }
    }
}
