pipeline {
  agent none

    stages {
        stage('Example Build') {
            agent { label 'master' }
            steps {
                sh 'echo "test"'
                sh 'python --version'
                sh 'python3 pythonscripthello.py'
            }
        }
    }
}
