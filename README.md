# Flask Demo App

This Repository host a demo Flask App, packaged as Docker container and deployed on AWS EC2 using a Jenkins pipeline.

The app exposes a single endpoint "\home" , which returns a response when accessed.

### Dependencies
1. Flask, Python
2. Docker
3. Docker hub
4. Ansible (ansible=2.9.23)
5. AWS
6. boto, boto3

### Set application locallly for development
1. Navigate to a directory where you want to clone the repository.
2. Clone the repository using https
3. Change directory into the project.
4. Create a virtual environment
```shell
python3.10 -m venv venv
```
6. Activate the Python virtual environment
```shell
source venv/bin/activate
```
7. Install the project's development requirements
```shell
pip install -r requirements/dev.txt
```
8. Run the application
```shell
python app.py
```

### Run tests
```shell
python test_app.py
```

### Jenkins server
To spin up the Jenkins server, you can either:
1. install all the required packages (jenkins, docker, python3, boto, boto3, ansible ....) on an new/existing instance
2. Use the provided Dockerfile to create a custom Jenkins container with the required dependencies
```shell
docker build -t custom-docker-jenkins -f Dockerfile.jenkins .
```
```shell
docker run -p 8080:8080 -p 50000:50000 -d -v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home custom-docker-jenkins
```

### Configuring Jenkins server
For the pipeline to run successfully, the following Docker plugins are required:
1. Docker Pipeline plugin
2. Docker Plugin
3. CloudBees Docker Build and Publish plugin
4. Ansible plugin

How to install the required plugins:
1. Open your Jenkins instance in a web browser and navigate to the Jenkins dashboard.

2. Click on "Manage Jenkins" on the left-hand side menu.

3. On the "Manage Jenkins" page, click on "Manage Plugins".

4. The "Plugin Manager" page will open, which has multiple tabs. By default, you'll be on the "Updates" tab.

5. Switch to the "Available" tab. This tab lists all the plugins available for installation.

6. In the search box at the top right corner, type the name of the plugin you want to install. For example, if you want to install the "Docker Pipeline Plugin", type "Docker Pipeline" in the search box.

7. The search results will display the matching plugins. Locate the desired plugin and check the checkbox next to its name.

8. Once you have selected the plugin(s) you want to install, scroll down to the bottom of the page.

9. Click on the "Install without restart" button. This option installs the plugin immediately without requiring a Jenkins restart.

To configure Jenkins to "listen" for changes on the specified git url:
1. Open your Jenkins instance in a web browser and navigate to the Jenkins dashboard.
2. Click on "New Item" to create a new Jenkins pipeline.
3. Enter a name for your pipeline
4. Select "Pipeline" as the project type and click on "OK".
5. On the pipeline configuration page, scroll down to the "Pipeline" section.
6. Choose "Pipeline script from SCM", you need to specify the SCM details, such as the Git URL, credentials, and branch.
7. choose "Git" as the SCM in the "SCM" dropdown.
8. Provide the Git repository URL of your project in the "Repository URL" field.
9. Specify the branch you want to monitor for changes in the "Branches to build" field. For your case, enter */main to listen for changes on the main branch.
10. Configure the credentials to access the Git repository if required. Click on "Add" next to the "Credentials" field and provide the necessary credentials information. (if it's a public repository this is not required.)
11. On the Build triggers tab, check the "GitHub hook trigger for GITScm polling" box to allow Github to push events trigger to the pipeline
12. Save the pipeline configuration by clicking on the "Save" or "Apply" button. 

### To create a Github-Jenkins webhook
1. In the repository settings, select "webhooks" under code and automation 
2. Append the “/github-webhook/” at the end of the Jenkin server Url
3. Select the “Content-type” to “application/json” format.
4. Next, check one option under “Which events would you like to trigger this webhook?“. "Just the Push Event": It will only send data when someone push into the repository.
5. click on the “Add Webhook” button to save Jenkins GitHub Webhook configurations.

### Boto package configuration
1. Change directory into the root folder
```shell
cd ~
```
2. Create a file in the root dir 
```shell
touch .boto
```
3. Add the following content in that file
```shell
[Credentials]
aws_access_key_id=<AWS-ACCCESS-KEY-ID.
aws_secret_access_key=<AWS-SECRET-ACCESS-KEY>
```

### AWS Configuration
1. Create an IAM user:
    1. Go to the AWS Management Console and navigate to the IAM service.
    2. Create a new IAM user or use an existing one.
    3. Assign the necessary IAM policies to the user to grant permissions for EC2 instance creation. For example, the user should have the "AmazonEC2FullAccess" policy attached.
2. Generate access keys for the IAM user:
    1. In the IAM user's "Security Credentials" tab, create or retrieve the access keys.
    2. Take note of the generated Access Key ID and Secret Access Key.
3. Configure AWS CLI on Jenkins server:
    1. Install AWS CLI on your Jenkins server if it's not already installed.
    2. Run the aws configure command on the Jenkins server and provide the Access Key ID, Secret Access Key, default region, and output format.

### Deployment
- Once the pipeline runs sucessfully, navigate to newly created instance
- copy the ***Public IPv4 DNS***, append port 5000 and path "/home"
- eg ec2-52-xxx-2x5-2x4.compute-1.amazonaws.com:5000/home
- Once the pipeline runs successfully, you should see something like this:
- ![sample output](https://res.cloudinary.com/melvinkimathi/image/upload/v1685274561/Screenshot_2023-05-28_at_12.09.49_xr14pl.png)
