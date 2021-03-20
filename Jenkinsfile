pipeline {
    agent {
      label 'agent1'
      }

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
              sh "s3 cp https://github.com/prakash0610/gitjenkinss3/* s3://pabugitjenkinss3/"

             }
          }
        }
    }
}
