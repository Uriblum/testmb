pipeline {
  agent none
  triggers { cron('* * * * *') }
    stages {
        stage('Example Build') {
            agent { label 'master' }
            steps {
                sh 'python pythonscripthello.py'
                sh 'sleep 30'
                sh 'python pythonscripthello.py'
            }
        }
    }
}
