pipeline {
  agent none

    stages {
        stage('Example Build') {
            agent { label 'Master' }
            steps {
                sh 'echo "test"'
            }
        }
    }
}
