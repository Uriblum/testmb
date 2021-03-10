pipeline {
  agent none

    stages {
        stage('Example Build') {
            agent { label 'Master' }
            steps {
                sh 'env'
                sh ' sleep 8'
            }
        }
        stage('Example Test') {
            agent { label 'Master' }
            steps {
                sh 'env'
                sh ' sleep 5'
            }
        }
    }
}
