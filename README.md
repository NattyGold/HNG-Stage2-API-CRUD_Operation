### Person API

## Introduction
#  HNG Backend Stage Two Task
You are to build a simple REST API capable of CRUD operations on a "person" resource, interfacing with any database of your choice. Your API should dynamically handle parameters, such as adding or retrieving a person by name. Accompany the development with UML diagrams to represent your system's design and database structure. Host your entire project on GitHub, and provide a well-structured documentation in the repository that outlines request/response formats, setup instructions, and sample API usage

## Task Breakdown: Develop a REST API with Basic CRUD Operation

Objective:

- Build a simple REST API capable of CRUD operations on a resource, say, a "person" \*
- The chosen programming language should interface with any chosen database of your choice

## Tech Stack (Dependencies)

### 1. Backend Dependencies

Our tech stack will include the following:

- **virtualenv** as a tool to create isolated Python environments
- **SQLAlchemy ORM** to be our ORM library of choice
- **PostgreSQL** as our database of choice
- **Python3** and **Flask** as our server language and server framework

You can download and install the dependencies mentioned above using `pip` as:

```
pip install virtualenv
pip install SQLAlchemy
pip install postgres
pip install Flask
```

> **Note** - If we do not mention the specific version of a package, then the default latest stable package will be installed.

## Main Files: Project Structure

```sh
├── app
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── person.py
├── config.py
```

## Here is a breakdown of each file:

** config.py has the configuration for the API.
** app/__init__.py is the file that contains database and application ** instances.
** app/models.py contains the database schema and the ORM.
** app/routes.py contains the API functions that the API will invoke.


## Instructions
1. Make sure you have python installed
2. Install all dependencies. pip install -r requirements.txt
3. set the database URL to the environment variable ``         DEV_DATABASE_URL,   which is the URL for the POSTGRES database. 
4. Run the following command on your terminal to define that env var:
$  set DEV_DATABASE_URL=postgresql://postgres:admin@localhost:5432/persondb
#  let's configure our flask app environment variable using this command:
5. $ SET FLASK_APP=person.py
6. $ SET FLASK_ENV=development
7. $ SET flask run

## Development Setup

1. **Download the project starter code locally**

```
git clone https://github.com/nattygold/hng-stage2.git
cd hng-stage2

2. **Initialize and activate a virtualenv using:**
```
python -m virtualenv env
source env/bin/activate

```
>**Note** - In Windows, the `env` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:
```

source env/Scripts/activate

```

4. **Install the dependencies:**
```

pip install -r requirements.txt

```

5. **Run the development server:**
```

export FLASK_APP=app.py
export FLASK_ENV=development # enables debug mode
python3 app.py

```

6. **Verify on the Browser**<br>
Navigate to project homepage [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://localhost:5000](http://localhost:5000)

```
