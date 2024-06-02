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
