# Modsen Practice (Python)
Проект для прохождения производственной практики в компании Modsen (Python department) <br /> 
Stack: Python, FastAPI, PostgreSQL, ElasticSearch.

### Commands to start the project:

`docker-compose up` <br>

Database table and elastic index creation will be done automatically. <br> 
Then program will fill them with the data from `posts.csv`. It will take some time...<br>
After success, you will be informed with such messages:

`INFO:     Application startup complete. `<br>
`Project initialization finished successfully!`

Now you can check documentation and test endpoints on the swagger:
### [Swagger](http://127.0.0.1:8000/docs)

### Hints:
1) If database table and elastic index filled successfully, `/get_items_amount` endpoint should return:<br>
{<br>
  "elastic": "index (name=posts) contains 1500 items!",<br>
  "database": "table (name=posts) contains 1500 items!"<br>
}
2) If container with elasticsearch closes unexpectedly, main problem usually is your memory limit for docker. 
<br>You should set >= 2.5 GB RAM for Docker daemon