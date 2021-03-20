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
              sh "echo %PATH%"
              sh "aws s3 ls"

             }
          }
        }
    }
}
