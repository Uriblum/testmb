pipeline {
  agent none

    stages {
        stage('Example Build') {
            agent { label 'master' }
            steps {
                sh 'echo "test"'
            }
        }
    }
}
