# DockerExample

## Description
This project is a Docker-compose setup for running a web application with a MySQL database. It consists of two services: `bd` for the MySQL database and `web` for the web application.

## Requirements
- Docker
- Docker Compose

## Installation and Setup
1. Clone this repository.
2. Navigate to the project directory.
3. Set up your environment variables in a `.env` file. Example:
    ```plaintext
    DB_NAME=mydatabase
    DB_USER=myuser
    DB_PASSWORD=mypassword
    DEBUG=True
    SECRET_KEY=mysecretkey
    DB_HOST=bd
    DB_PORT=3306
    ```
4. Run the following command to start the services:
    ```bash
    docker-compose up
    ```

## Configuration
### Database Service (`bd`)
- Image: MySQL
- Exposed Port: 3306
- Environment Variables:
    - MYSQL_DATABASE: Name of the database
    - MYSQL_USER: Username for the database
    - MYSQL_PASSWORD: Password for the database user
    - MYSQL_ROOT_PASSWORD: Root password for MySQL
- Health Check:
    - Checks MySQL connection using `mysqladmin ping`
    - Interval: 10 seconds
    - Timeout: 5 seconds
    - Retries: 5

### Web Service (`web`)
- Build: Current directory
- Volumes: Mounts the current directory to `/code` in the container
- Environment Variables:
    - DEBUG: Debug mode for the web application
    - SECRET_KEY: Secret key for the Django application
    - DATABASE_NAME: Name of the database
    - DATABASE_USER: Username for the database
    - DATABASE_PASSWORD: Password for the database user
    - DATABASE_HOST: Hostname of the database service (`bd`)
    - DATABASE_PORT: Port of the database service (`bd`)
- Exposed Port: 8000
- Depends On: `bd` service with a condition for service healthiness

## Usage
- Access the web application at `http://localhost:8000`.

## Persistence
- Database data is stored in a named volume `db-data`.

## Contributing
Feel free to contribute by submitting issues or pull requests.

## License
This project is licensed under the [MIT License](LICENSE).
