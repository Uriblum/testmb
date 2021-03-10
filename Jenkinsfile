pipeline {
  agent none
  triggers { cron('* * * * *') }
    stages {
        stage('Example Build') {
            agent { label 'master' }
            steps {
                sh 'echo "test"'
                sh 'python --version'
                sh 'python pythonscripthello.py'
            }
        }
    }
}
