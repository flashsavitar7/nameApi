# NameApi API Documentation

The NamesOfPips API is a simple RESTful API for managing a list of people's names. It allows you to perform basic CRUD (Create, Read, Update, Delete) operations on individual records in the database.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [Create a Person](#create-a-person)
  - [Read a Person](#read-a-person)
  - [Update a Person](#update-a-person)
  - [Delete a Person](#delete-a-person)
- [Request/Response Formats](#requestresponse-formats)
- [Sample API Usage](#sample-api-usage)
- [Testing](#testing)

## Getting Started

### Prerequisites

Before you can use the NameApi API, ensure you have the following prerequisites installed on your system:

- Python 3.x
- Flask
- Flask-SQLAlchemy
- PostgreSQL (or any database of your choice)

### Installation Locally

* please note that this step is only if you want to run it locally on your device . The flask app is currently live and you can perform all testing operations using this link:
* https://nameapi-mnmf.onrender.com/api

1. Clone the repository:
git clone https://github.com/your-username/NameApi.git


2. Install Python dependencies:
pip install -r requirements.txt 



3. Set up your database:

- Create a PostgreSQL database and configure the connection URI in the Flask app. You can do this in the `app.py` file.

4. Run the Flask application:
puthon app.py


Your API should now be running locally on `http://localhost:5000`.

## API Endpoints

### Create a Person

- **Endpoint**: `/api`
- **HTTP Method**: POST
- **Description**: Add a new person.
- **Request Body**:
- JSON object with the following structure:
 ```json
 {
   "name": "John Doe"
 }
 ```
- The "name" field is required and should be a string representing the person's name.
- **Response**:
- HTTP Status: 201 (Created)
- JSON object:
 ```json
 {
   "message": "Person created successfully"
 }
 ```

### Read a Person

- **Endpoint**: `/api/<int:user_id>`
- **HTTP Method**: GET
- **Description**: Fetch details of a person by their user ID.
- **Response**:
- HTTP Status: 200 (OK) if the person is found.
- HTTP Status: 404 (Not Found) if the person does not exist.
- JSON object:
 ```json
 {
   "id": 1,
   "name": "John Doe"
 }
 ```

### Update a Person

- **Endpoint**: `/api/<int:user_id>`
- **HTTP Method**: PUT
- **Description**: Modify details of an existing person by their user ID.
- **Request Body**:
- JSON object with the following structure:
 ```json
 {
   "name": "Jane Doe"
 }
 ```
- The "name" field is required and should be a string representing the updated name.
- **Response**:
- HTTP Status: 200 (OK) if the person is found and updated.
- HTTP Status: 404 (Not Found) if the person does not exist.
- JSON object:
 ```json
 {
   "message": "Person updated successfully"
 }
 ```

### Delete a Person

- **Endpoint**: `/api/<int:user_id>`
- **HTTP Method**: DELETE
- **Description**: Remove a person by their user ID.
- **Response**:
- HTTP Status: 200 (OK) if the person is found and deleted.
- HTTP Status: 404 (Not Found) if the person does not exist.
- JSON object:
 ```json
 {
   "message": "Person deleted successfully"
 }
 ```

## Request/Response Formats

- **Request Format**: All requests must be in JSON format with the appropriate fields as described in the API endpoints section.

- **Response Format**: The API returns responses in JSON format. Successful responses include a relevant message or data, and error responses include an error message.

## Sample API Usage

Here are some sample API usage scenarios using CURL Format:

- **Creating a Person**:

curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe"}' http://localhost:5000/api

- **Reading a Person**:

curl http://localhost:5000/api/1


- **Updating a Person**:

curl -X PUT -H "Content-Type: application/json" -d '{"name": "Jane Doe"}' http://localhost:5000/api/1



- **Deleting a Person**:

curl -X DELETE http://localhost:5000/api/1



## Testing

You can test the NamesApi API using automated test scripts. hust python test.py .





