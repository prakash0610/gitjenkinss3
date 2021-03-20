pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps{
                checkout scm
            }

        }
        stage('Build') {
            steps{
                sh "ls -latr"
            }
        }
        stage('Copy') {
          steps{
            withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'awsjenkins', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
              sh "/usr/local/bin/aws s3 ls"
              sh "/usr/local/bin/aws s3 cp https://github.com/prakash0610/gitjenkinss3/* pabugitjenkinss3"
              sh 's3Upload(file:'https://github.com/prakash0610/gitjenkinss3/*', bucket:'pabugitjenkinss3', path:'/myfiles')'
             }
          }
        }
    }
}
