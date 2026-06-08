FROM ubuntu:22.04

RUN apt-get update
RUN apt-get install -y openjdk-21-jdk maven

WORKDIR /app

COPY . .

# compile inside container
RUN mvn clean package

# run the built jar (adjust name if needed)
CMD ["java", "-jar", "target/hibernate-sqlite-1.0-SNAPSHOT.jar"]