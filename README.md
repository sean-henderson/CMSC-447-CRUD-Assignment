# CMSC-447-CRUD-Assignment
This is HW2 for CMSC 447, Spring 2023. It is for practicing CRUD operations on a database via an application developed with a combination of frameworks and modules. This repo assumes you have all of the requisite packages and applications installed. MySQL Workbench was used to test the workings (specifically the backend, since the user interface is not ready) of this assignment.

This homework assignment is somewhat incomplete. The following should be expected from what is present in this repository:
- The beginnings to a reactjs implementation but not much
- A functional Flask application that can update, add, display, and delete entries in a MySQL database
- An attempt at a user interface (see templates/index.html to see what I attempted to do)

This assignment assumes that the MySQL database "447_hw2" has already been created. Change mysql_password in db.yaml to whatever your password is for your hosted database. The SQL script to create this database can be found at SQL/create_db.sql. Once the database has been created, cd to the venv folder and run 'flask run.'

Now, you should be able to open the Flask application in your web browser. The terminal will have told you what you should type in to your browser for it to open. Unfortunately, however, due to the unfinished nature of this submission, there is not much to see.
