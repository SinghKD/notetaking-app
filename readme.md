# Note Taking API

A simple RESTful API for a note taking app built with Django and Django REST framework.

## Features

- Create, Read, Update, Delete operations for notes
- Pinning/unpinning of notes

## Requirements

- Python 3.8 or later
- Django 3.2 or later
- Django REST Framework 3.12 or later

## Quick Start

- Clone the repository

```bash
git clone https://github.com/username/notetaking_app.git
cd notetaking_app
```

- Install the requirements

```bash
pip install -r requirements.txt
```

- Apply migrations and run the server

```bash
python manage.py migrate
python manage.py runserver
```

You can now access the API at `localhost:8000`.

## Endpoints

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/28730127-6933b2a2-b84a-4228-a9ba-3e0064f98cb5?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D28730127-6933b2a2-b84a-4228-a9ba-3e0064f98cb5%26entityType%3Dcollection%26workspaceId%3D871cfd80-dfe2-4caa-ad11-87a16ca8fec0)

Deployed url: https://notetaking-app.fly.dev/notes/

The notetaking app supports the following API endpoints:

1. Create Note
Endpoint: /create/
Method: POST
Data Params: title, content, image
Success Response: HTTP 201 Created
Error Response: HTTP 400 Bad Request
Description: This endpoint is used to create a new note. The title and content are mandatory fields, while the image is optional. The image file must meet specific validation criteria regarding size, format, and filename.

2. List Notes
Endpoint: /list/
Method: GET
Success Response: HTTP 200 OK
Description: This endpoint is used to get a list of all existing notes.

3. Pin Note
Endpoint: /pin/<int:pk>/
Method: PATCH
URL Params: id=[integer]
Success Response: HTTP 200 OK
Error Response: HTTP 404 Not Found
Description: This endpoint is used to pin or unpin a note. The note's pinned status will be toggled each time this endpoint is called.

4. Delete Note
Endpoint: /delete/<int:pk>/
Method: DELETE
URL Params: id=[integer]
Success Response: HTTP 204 No Content
Error Response: HTTP 404 Not Found
Description: This endpoint is used to delete a note.

5. Update Note
Endpoint: /update/<int:pk>/
Method: PUT
URL Params: id=[integer]
Data Params: title, content, image
Success Response: HTTP 200 OK
Error Response: HTTP 404 Not Found or HTTP 400 Bad Request
Description: This endpoint is used to update an existing note. The title, content, and image are all optional fields in the request. However, if an image is provided, it must meet specific validation criteria regarding size, format, and filename.
Please replace <int:pk> with the ID of the note that you want to interact with.

Remember that these endpoints only support JSON responses.

## Tests

This API includes a suite of tests. Run them using Django's test framework:

```bash
python manage.py test
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the terms of the MIT license.

## Known bugs

- Image is not optional right now.
- While deploying without volumes on fly.io you would need to :
  - `fly ssh console -s -C "python manage.py migrate"` for some reason.