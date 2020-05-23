pipeline{
        agent any
        stages{
            stage('build'){
                steps{
                    sh "ssh craft@craft << EOF \
                        docker rm -f $(docker ps --all -q) \
                        docker rmi -f $(docker images -q) \
                        rm -rf SOFIA-project-2 \
                        git clone https://github.com/Alexandracope/SOFIA-project-2.git \
                        cd SOFIA-project-2 \
                        docker-compose build \
                        EOF"
                }
            }
            stage('Deploy'){
                steps{
                    sh "ssh craft@craft << EOF \
                        docker login -u yasirsatti -p Mstr00slv# \
                        docker push yasirsatti/craft-srv1 \
                        docker push yasirsatti/craft-srv2 \
                        docker push yasirsatti/craft-srv3 \
                        docker push yasirsatti/craft-srv4 \
                        EOF"
                }
            }
        }    
}