pipeline {
    agent {
        docker { image 'python:3.9' }
    }
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
                sh 'pip install -r scratch_fw_pytest/requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest -v scratch_fw_pytest/tests/'
            }
        }
    }
}
