I was on the wrong user when I tired to make the read me... Realized only today.

Requirements: Install python 3.7 (or via VENV) or higher, Docker, Jenkins if you are working locally or connect your jenkins machine to this repo.

 The script will get the exhange rate to a defined currency (can be edited in the script, best practice would be to have a file to edit the variables)
 and return the names of those that are below 10. To run the test script use command line in script's directory:
 python currency_rate_checker.py

 The test checks if the currencies in the result are below 10. To run the test script use command line in script's directory:
 python test_currency_rate_checker.py

 To launch the jenkins in docker: first run a docker container with the next command: 
 docker network create jenkins
 and  
   docker run \
   --name jenkins-docker \
   --rm \
   --detach \
   --privileged \
   --network jenkins \
   --network-alias docker \
   --env DOCKER_TLS_CERTDIR=/certs \
   --volume jenkins-docker-certs:/certs/client \
   --volume jenkins-data:/var/jenkins_home \
   --publish 2376:2376 \
   docker:dind \
   --storage-driver overlay2

 Run the next command in the Dockerfile directory "docker build -t jenkins_for_devalore"
 In same directory run 

   docker run \
   --name jenkins-blueocean \
   --restart=on-failure \
   --detach \
   --network jenkins \
   --env DOCKER_HOST=tcp://docker:2376 \
   --env DOCKER_CERT_PATH=/certs/client \
   --env DOCKER_TLS_VERIFY=1 \
   --publish 8080:8080 \
   --publish 50000:50000 \
   --volume jenkins-data:/var/jenkins_home \
   --volume jenkins-docker-certs:/certs/client:ro \
   jenkins_for_devalore        


 Jenkins should be running on the local host on port 8080 - http://localhost:8080

 In jenkins, click on "create new job" and give it a name and specify it is a github project.
 Copy github's URL to the field.
 In "Build steps" check Shell Command and paste the next snippet

 IMAGE_NAME="docker:dind"
 CONTAINER_NAME="jenkins-docker"
 echo "Check current working directory"
 pwd
 echo "Build docker image and run container"
 docker build -t $IMAGE_NAME .
 docker run -d --name $CONTAINER_NAME $IMAGE_NAME
 echo "Copy result.xml into Jenkins container"
 rm -rf reports; mkdir reports
 docker cp $CONTAINER_NAME:/python-test-calculator/reports/result.xml reports/
 echo "Cleanup"
 docker stop $CONTAINER_NAME
 docker rm $CONTAINER_NAME
 docker rmi $IMAGE_NAME
