# clonecode-backend
## Setup
### Pre-requisites
- [Poetry](https://python-poetry.org/docs/#installation)
- Python 3.9
- MySQL
  - for Docker: `docker run -e MYSQL_ROOT_PASSWORD=strongpassword -p 3306:3306 -d mysql:8.0`

### Installation
- Clone the repository
- Run `poetry install` to install dependencies

### Environment Variables
- `DB_CONNECTION_STRING` - The URL of the database to connect to
  - Example: `mysql://user:password@127.0.0.1:3306/clonecode`

### Running the server
- Run `poetry run uvicorn src.app.application:app --reload` to start the server
