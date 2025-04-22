FROM postgres:latest

# Copy the SQL script to initialize the database
COPY synthetic_consent_data.sql /docker-entrypoint-initdb.d/

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=your_username
ENV POSTGRES_PASSWORD=your_password
ENV POSTGRES_DB=your_database

# The SQL script will be executed automatically on container startup
