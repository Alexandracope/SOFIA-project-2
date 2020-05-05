pipeline{
        agent any
        stages{
            stage('Build Image'){
                steps{
                    sh "sudo docker build -t craft ."
                }
            }
            stage('Clean'){
                steps{
                    sh label: '', script: '''if [ "$(sudo docker ps -aq -f name=sofia_project2_service1)" ]; then
                        sudo docker rm -f sofia_project2_service1
                    fi'''
                    }
                }
            stage('Run Container'){
                steps{
                    sh "sudo docker run -d --name sofia_project2_service1 -p 80:80 craft"
                }
            }
        }    
}