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
              git branch: 'main', credentialsId: 'pabugithubid', url: 'https://github.com/prakash0610/gitjenkinss3.git'
              sh "/usr/local/bin/aws s3 ls"
              sh 's3Upload(file:'url', bucket:'pabugitjenkinss3', path:'/myfiles')'
             }
          }
        }
    }
}
