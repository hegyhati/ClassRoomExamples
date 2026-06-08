# ===== BUILD STAGE =====
FROM maven:3.9-eclipse-temurin-21 AS build

WORKDIR /app

COPY pom.xml .
COPY src ./src

RUN mvn clean package -DskipTests


# ===== RUNTIME STAGE =====
FROM eclipse-temurin:21-jre

WORKDIR /app


# main jar
COPY --from=build /app/target/hibernate-sqlite-1.0-SNAPSHOT.jar app.jar

# dependency jars 
COPY --from=build /app/target/lib ./lib

# run with classpath
ENTRYPOINT ["sh", "-c", "java -cp 'app.jar:lib/*' com.example.hibernate.Main"]


