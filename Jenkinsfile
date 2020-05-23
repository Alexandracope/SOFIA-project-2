pipeline{
        agent any
        stages{
            stage('build'){
                steps{
                    sh "ssh craft@craft docker rm -f $(docker ps --all -q)"
                    sh "ssh craft@craft docker rmi -f $(docker images -q)"
                    sh "ssh craft@craft rm -rf SOFIA-project-2"
                    sh "ssh craft@craft git clone -b development-yasir https://github.com/Alexandracope/SOFIA-project-2.git"
                    sh "ssh craft@craft cd SOFIA-project-2"
                    sh "ssh craft@craft docker-compose build"
                }
            }
            stage('Deploy'){
                steps{
                    sh "ssh craft@craft docker login -u yasirsatti -p Mstr00slv#"
                    sh "ssh craft@craft docker push yasirsatti/craft-srv1"
                    sh "ssh craft@craft docker push yasirsatti/craft-srv2"
                    sh "ssh craft@craft docker push yasirsatti/craft-srv3"
                    sh "ssh craft@craft docker push yasirsatti/craft-srv4"
                }
            }
        }    
}