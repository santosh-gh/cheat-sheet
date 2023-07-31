# Install Jenkins on AWS EC2 Instance
  Jenkins is an open source automation server written in Java. Basically, Jenkins provides a continuous integration (CI) and continuous delivery (CD) solution to accelerate the software delivery process.

# Launch a Linux EC2 Instance and configure security group.

# Update the installed packages
  sudo su yum update

# Install Java 8
  java -version

  yum install java-1.8.0

# Install Jenkins
  1.) Download the latest Jenkins package from the Red Hat Repository
 
      wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat/jenkins.repo

  2.) Import the verification key using the package manager RPM

      rpm --import https://pkg.jenkins.io/redhat/jenkins.io.key

      Note: If you've previously imported the key from Jenkins, the "rpm --import" will fail because you already have a key. Please ignore that and move on.

  3.) Install the Jenkins package by issuing the following command

      yum install -y jenkins

# Start Jenkins Service
  You can start the jenkins service by issuing the following command

  service jenkins start

# Check Jenkins Installation
  You can check the Jenkins process running on your server by issuing the following command

  ps -aux | grep jenkins

# Auto-Start Jenkins Service on system reboot
  You can ensure that Jenkins will start following a system reboot by issuing the following command

  chkconfig jenkins on

# Stop Jenkins Service
  As needed, you can stop the Jenkins process by issuing the following command

  service jenkins stop

# Restart Jenkins Service
  You can restart the Jenkins process by issuing the following command
  
  service jenkins restart

# Configure Jenkins
  1.) Access Jenkins through browser

      http://YOUR-SERVER-PUBLIC-IP:8080

  2.) Now copy the default admin password and paste it to unblock the Jenkins

      cat /var/lib/jenkins/secrets/initialAdminPassword

  3.) Choose install suggested plugins  

  4.) Create your first admin user