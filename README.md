# Crowdfundr

Crowdfundr is a university project developed by four students as part of NF18, a database course at UTC. The goal was to design and implement the database side of a crowdfunding platform, first with a relational model and then with a MongoDB model.

## Overview

The subject was given by the course staff: CrowdFundr is a modern crowdfunding platform that needs to manage submitted projects, creator teams, financial contributions, rewards, reviews, and users. Our work was to understand these needs and turn them into database models, schemas, data scripts, and small command-line applications.

During the project, we produced several deliverables: UML diagrams, relational models, SQL schema files, data manipulation scripts, and a Python CLI application. A second part of the project explores a NoSQL version using MongoDB scripts and a small Python menu.

The repository has been cleaned up so both the SQL and NoSQL applications can be launched with Docker.

## Tech Stack

- Python
- PostgreSQL
- MongoDB
- Docker / Docker Compose
- SQL
- JavaScript Mongo shell scripts
- psycopg2

## Features

- Manage crowdfunding projects, contributors, members, contributions, rewards, reviews, NGOs, carriers, and incubators
- Use a Python CLI to interact with the PostgreSQL database
- Run contributor and admin workflows from terminal menus
- Execute the three analytical queries required by the course
- Load and query a MongoDB version of the data model
- Run both the SQL and NoSQL applications with Docker Compose

## Project Structure

```text
.
|-- Application/          Python CLI for the PostgreSQL application
|-- Application/db_functions/
|   `-- ...               Database functions used by the SQL CLI
|-- LDD/                  SQL schema creation scripts
|-- LMD/                  SQL insert, update, delete, and select scripts
|-- MLD/                  Relational model files
|-- NoSQL/                MongoDB version of the project
|-- NoSQL/Application/    Mongo scripts and Python CLI for the NoSQL app
|-- Scripts/              Helper SQL scripts used during development
|-- UML/                  UML diagrams for the SQL model
|-- Dockerfile            Docker image for the SQL Python app
|-- NoSQL/Dockerfile      Docker image for the NoSQL Python app
`-- docker-compose.yml    PostgreSQL, MongoDB, and app services
```

## Getting Started

You need Docker and Docker Compose installed.

Start the databases:

```bash
docker compose up -d postgres mongo
```

Run the SQL application:

```bash
docker compose run --rm app
```

Run the NoSQL application:

```bash
docker compose run --rm mongo-app
```

You can also run all NoSQL scripts directly:

```bash
docker compose exec mongo mongosh "mongodb://localhost:27017" /scripts/application.js
```

Stop the containers:

```bash
docker compose down
```

Reset all database data:

```bash
docker compose down -v
```

PostgreSQL is exposed on `localhost:5433`, and MongoDB is exposed on `localhost:27017`.

## Configuration

The `.env.example` file documents the main environment variables:

| Variable | Purpose |
| --- | --- |
| `CROWDFUNDR_DB_HOST` | PostgreSQL host |
| `CROWDFUNDR_DB_PORT` | PostgreSQL port |
| `CROWDFUNDR_DB_NAME` | PostgreSQL database name |
| `CROWDFUNDR_DB_USER` | PostgreSQL username |
| `CROWDFUNDR_DB_PASSWORD` | PostgreSQL password |
| `CROWDFUNDR_DB_SCHEMA` | PostgreSQL schema used by the application |
| `MONGODB_URI` | MongoDB connection URI |

## Database Model

The SQL UML diagram is available in `UML/UMV3L.png`.

The NoSQL UML diagram is available in `NoSQL/UML/UMLV1.png`.

The PostgreSQL schema is created from `LDD/LDD_V1.sql`, and the initial SQL data is loaded from `LMD/INSERT.sql`.

## Example Queries / Use Cases

The SQL application includes two main modes:

- Contributor mode: log in as a contributor, display personal information, create a contribution, manage rewards, and add, update, or delete reviews.
- Admin mode: manage users, members, projects, project members, contributions, rewards, carriers, NGOs, social project/NGO links, incubators, and reviews.

The SQL menu also includes three analytical queries:

- Find artistic projects involving two selected members that have reached their funding goal.
- Compute the average review score for social projects supported by a selected NGO, while only considering contributors above a chosen contribution amount.
- Count distinct contributors who claimed a physical reward shipped by a selected carrier for projects linked to an incubator.

The NoSQL application includes similar MongoDB use cases:

- Insert the normalized MongoDB collections for projects, contributors, and members.
- Delete or update a review in a project document.
- Display the members linked to a project.
- Run the same three analytical queries with MongoDB aggregation pipelines.

## What This Project Demonstrates

- Relational database design
- SQL schema design and implementation
- Data integrity and constraint management
- Python/PostgreSQL integration
- MongoDB scripting and aggregation queries
- Dockerized local development environment
- Basic CLI application structure

## My Contributions

This project was developed by a team of four students. My main contributions were:

- Building and refactoring a large part of the Python CLI used to interact with the PostgreSQL database.
- Implementing several CRUD features for contributors, projects, contributions, rewards, carriers, NGOs, incubators, and related entities.
- Making the required SQL analytical queries interactive from the application menu.
- Working on the NoSQL model and MongoDB scripts, including the insertion script, update/delete scripts, and aggregation queries.
- Restructuring the NoSQL application into smaller scripts to make it easier to read and run.
- Cleaning up the repository after the course so the project can be launched with Docker.

## Limitations

- No web API yet
- No authentication layer
- No automated test suite yet
- CLI-oriented application
- Academic project scope
