##  API Documentation
#   This documentation provides information about the API endpoints available in the code snippet provided.
#   Base URL
    The base URL for accessing the API endpoints is `http://localhost:5000/`.

###   1. Create a Person
**Endpoint:** `/api/person`
**Method:** `POST`
This endpoint is used to create a new person.
##  Request Body
The request body should be a JSON object with the following properties:
- `first_name` (string, required): The first name of the person.
- `last_name` (string, required): The last name of the person.
- `age` (integer, required): The age of the person.
##  Response
- Status Code: 201 (Created)
- Response Body: A JSON object representing the created person and a success message.
Example:
```json
{
"first_name": "Nathaniel",
"last_name": "Asa",
"age": 25
}
```
### 2. Get a Person by ID
**Endpoint:** `/api/person/<int:id>`
**Method:** `GET`
This endpoint is used to retrieve a person by their ID.
Path Parameters
- `id` (integer, required): The ID of the person to retrieve.
Response
- Status Code: 200 (OK)
- Response Body: A JSON object representing the person.
```json
{
    "age": 11,
    "first_name": "natty",
    "id": 1,
    "last_name": "gold"
}
```

### 3. Update a Person
**Endpoint:** `/api/person/update/<int:id>`
**Method:** `PUT`
This endpoint is used to update an existing person.
Path Parameters
- `id` (integer, required): The ID of the person to update.
Request Body
The request body should be a JSON object with the following properties:
- `first_name` (string, optional): The updated first name of the person.
- `last_name` (string, optional): The updated last name of the person.
- `age` (integer, optional): The updated age of the person.
Response
- Status Code: 200 (OK)
- Response Body: A JSON object representing the updated person and a success message.
Example:
```json
{
"first_name": "Olamide",
"last_name": "Adeleke",
"age": 30
}
```
### 4. Delete a Person
**Endpoint:** `/api/person/<int:id>`
**Method:** `DELETE`
This endpoint is used to delete a person by their ID.
Path Parameters
- `id` (integer, required): The ID of the person to delete.
Response
- Status Code: 200 (OK)
- Response Body: A JSON object with a success message indicating that the person has been deleted.
---

This documentation file provides an overview of the API endpoints, request/response formats, sample usage. Users can refer to this documentation to interact with the API effectively.
