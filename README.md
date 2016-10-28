# MFproject

Simple django webapp to demo api's for querying different schemes.
The schemes are  provided in a file with a pre-defined format.
Check file 'NAV0.txt' under wsgi/project folder for example.

To deploy the app locally follow the following steps:

1. create a database with name 'demo'. Here we are using sqlite3 db to keep things simple.
2. run `python manage.py syncdb` from wsgi/project folder to synch database
3. run `python manage.py rip_file <filename>` ex: python manage.py rip_file NAV0.txt to populate entries in the DB.
4. run `python manage.py runserver` to start the server
5. visit the following urls

  http://localhost:8000/schemes/?category=<category_name>
  ex: http://localhost:8000/schemes/?category=Open Ended Schemes(Balanced)

  http://localhost:8000/schemes/<scheme_id>
  ex: http://localhost:8000/schemes/135760/

A routine is written to process the input file containing information about different schemas and populate the entries in the DB.
One can find the code located at file 'wsgi/project/mfapp/management/commands/rip_file.py'.
