pipeline{
        agent any
        stages{
            stage('build'){
                steps{
                    sh """
                        ssh craft@craft  << EOF
                        rm -rf SOFIA-project-2
                        git clone -b development-yasir https://github.com/Alexandracope/SOFIA-project-2.git
                        cd SOFIA-project-2
                        docker-compose build
                        docker login -u yasirsatti -p Mstr00slv#
                        docker push yasirsatti/craft-srv1
                        docker push yasirsatti/craft-srv2
                        docker push yasirsatti/craft-srv3
                        docker push yasirsatti/craft-srv4
                    """
                }
            }
            stage('Deploy'){
                steps{
                    sh """ 
                        ssh craft@craft << EOF
                        cd SOFIA-project-2
                        kubectl create -f craft.yaml
                    """
                }
            }
        }    
}