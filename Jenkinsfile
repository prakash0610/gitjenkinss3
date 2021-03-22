pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps{
                checkout scm
            }

        }
        stage('Test') {
            steps{
                sh "ls -latr"
                sh "pwd"
            }
        }
        stage('Copy') {
          steps{
            withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'awsjenkins', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
              sh "/usr/local/bin/aws s3 ls"
              sh "/usr/local/bin/aws s3 sync . s3://pabugitjenkinss3/myfiles/ --delete"
             }
          }
        }
    }
    post {
      always {
        emailext body: 'done', subject: 'copy to s3 success', to: 'prabhattarai1992@gmail.com'
      }
    }
}
