start_jenkins_server:
	docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk11
install_python_in_the_jenkins_container:
	docker exec -it -u 0 362d2b94f69f /bin/bash && \
		apt-get update && \
			apt-get install -y python3
build_docker_image:
	docker build -t test-flask-app:v1 .