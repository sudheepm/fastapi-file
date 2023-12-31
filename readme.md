# FastAPI File Operation Microservice

This is a FastAPI microservice for performing file operations including checking if a file exists.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7 or higher
- pip (Python Package Installer)

### Setup and Installation

1. Clone this repository to your local machine.

```shell
git clone https://github.com/sudheepm/fastapi-file.git
```

2. Navigate to the project directory:

```shell
cd fastapi-file
```

3. Create a virtual environment:

On Windows:

```shell
python -m venv env
```

On MacOS/Linux:

```shell
python3 -m venv env
```

4. Activate the virtual environment:

On Windows:

```shell
.\env\Scripts\activate
```

On MacOS/Linux:

```shell
source env/bin/activate
```

5. Install the necessary packages using pip:

```shell
pip install -r requirements.txt
```

### Running the Application

To run the FastAPI application, use the following command:

```shell
uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`.



### Testing with Swagger UI

FastAPI automatically generates a Swagger UI for your API. To access it, navigate to `http://localhost:8000/docs` in your web browser.



### Testing with curl

Here's an example command to test the API with curl:

```shell
curl -X POST "http://localhost:8000/file_operation" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"operation\":\"check_exists\",\"file_path\":\"/path/to/file\"}"
```

Replace `"/path/to/file"` with the path to the file you want to check.

The successful response in case the file is available  should be similar to:

```json
{
  "status": "success",
  "exists": true
}
```

The successful response in case the file is not available  should be similar to:

```json
{
  "status": "success",
  "exists": false
}
```

An unsuccessful response may look like:

```json
{
  "status": "failure",
  "error": "An error message"
}
```