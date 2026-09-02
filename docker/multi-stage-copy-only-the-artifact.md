# Multi-stage builds save nothing unless you copy only the artifact

*2026-09-01*

I assumed adding a second `FROM` was what made an image smaller. It is not - the saving comes
entirely from being specific about what crosses the stage boundary.

Same Dockerfile, two `COPY` lines, wildly different results:

```dockerfile
FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /src
COPY . .
RUN mvn -B clean package -DskipTests

FROM eclipse-temurin:21-jre-alpine
COPY --from=build /src/target/app-1.0.jar app.jar   # 187 MB
# COPY --from=build /src /app                       # 742 MB - the whole build tree
```

The second version still has two stages, still "uses multi-stage", and ships the compiler,
the source and the `.m2` cache anyway.

**Why it surprised me:** the syntax gets all the attention, but the win is a discipline
question - name the artifact, not the directory.

**Source:** measured on a real Spring Boot service
