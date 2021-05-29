pipeline {
    agent any
    stages {
        stage('Test') {
            agent {
                docker { image 'python:3.8' }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python -m unittest'
            }
        }
        stage('Deploy') {
            steps {
                script {
                    docker.withRegistry('https://082272919318.dkr.ecr.eu-west-3.amazonaws.com', 'ecr:eu-west-3:aws.dieter.jordens') {
                        def myImage = docker.build('aws-lambda-add-article')
                        myImage.push('latest')
                    }
                }
            }
        }
    }
}