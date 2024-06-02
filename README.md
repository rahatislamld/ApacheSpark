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

