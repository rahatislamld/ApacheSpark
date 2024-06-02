# Setting Up Apache Spark on EC2 Instance

This guide provides steps to set up Apache Spark on an EC2 instance and run a simple Spark application.

## Prerequisites

Ensure have the following prerequisites:

- An EC2 instance running Ubuntu
- Appropriate IAM role with necessary permissions
- Basic understanding of Linux commands

## Installation Steps

### 1. Connect to your EC2 Instance

Use SSH to connect to your EC2 instance:

```bash
ssh -i your-key.pem ubuntu@your-ec2-instance-ip
```
### 2. Install Java

Update the package list and install OpenJDK 11:

```sh
sudo apt update
sudo apt install openjdk-11-jdk -y
java -version
```
### 3. Install Scala

Update the package list and install Scala:

```sh
sudo apt update
sudo apt install scala -y
scala -version
```
### 4. Install Apache Spark

Download and extract Apache Spark:

```sh
sudo wget https://dlcdn.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz
tar xvf spark-3.5.1-bin-hadoop3.tgz
sudo mv spark-3.5.1-bin-hadoop3 /opt/spark
```

### 5. Configure Environment Variables

Edit ~/.bashrc file to add the environment variables:

```sh
nano ~/.bashrc
```
Add the following lines:
```sh
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export SCALA_HOME=/usr/share/scala
export SPARK_HOME=/opt/spark
export PATH=$PATH:$JAVA_HOME/bin:$SCALA_HOME/bin:$SPARK_HOME/bin
```
Source the .bashrc file to apply the changes:

```sh
source ~/.bashrc
```

### 6. Test Spark Shell

Verify the Spark installation by launching the Spark shell:

```sh
spark-shell
```

### 7. Install sbt (Scala Build Tool)

Add sbt's repository and install sbt:
```sh
sudo apt update
sudo apt-get install apt-transport-https curl gnupg -yqq
echo "deb https://repo.scala-sbt.org/scalasbt/debian all main" | sudo tee /etc/apt/sources.list.d/sbt.list
curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | sudo -H gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/scalasbt-release.gpg --import
sudo chmod 644 /etc/apt/trusted.gpg.d/scalasbt-release.gpg
sudo apt-get update
sudo apt-get install sbt
```
### 8.Run the Spark Application
Create a Python script for Spark application
```sh
nano spark_example.py
```
add code to the file

Submit the Spark application:
```sh
spark-submit spark_example.py
```

### Conclusion
This README provides a complete guide to set up Apache Spark, Java, Scala, and sbt on Ubuntu, and demonstrates how to run a simple Spark application using spark-submit. Follow the steps carefully to ensure successful setup and execution.
