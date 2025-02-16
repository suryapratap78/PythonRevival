pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/suryapratap78/PythonRevival.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r scratch_fw_pytest/requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest scratch_fw_pytest/tests/'
            }
        }
    }
}
