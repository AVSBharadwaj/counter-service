# A basic counter-service using
GitHub Actions, Docker, AWS services (ECR, EC2), Flask

1. This app keeps track of a counter, which is displayed for a GET request to the app and is increased by 1 for a POST request. The application is written in python with the flask framework. 
2. Then the application is containerised using docker to make it portable. A Dockerfile is written for the same. 
3. And finally a github action workflow is written to build the docker image and push it to Amazon ECR
