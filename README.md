# Spark Setup and Example

This guide provides steps to set up Apache Spark with Java and Scala on Ubuntu, and how to run a simple Spark application using `spark-submit`.

## Prerequisites

Ensure your system has the following installed:
- Ubuntu (20.04 or later)
- Curl
- GNU Privacy Guard (GPG)

## Installation Steps

### 1. Install Java

Update the package list and install OpenJDK 11:

```sh
sudo apt update
sudo apt install openjdk-11-jdk -y
java -version
```
### 2. Install Scala

Update the package list and install Scala:

```sh
sudo apt update
sudo apt install scala -y
scala -version
```
### 3. Install Apache Spark

Download and extract Apache Spark:

```sh
sudo wget https://dlcdn.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz
tar xvf spark-3.5.1-bin-hadoop3.tgz
sudo mv spark-3.5.1-bin-hadoop3 /opt/spark
```

### 4. Configure Environment Variables

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

### 5. Test Spark Shell

Verify the Spark installation by launching the Spark shell:

```sh
spark-shell
```

### 6. Install sbt (Scala Build Tool)

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
### 7.Run the Spark Application
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
