
##Loading data
 just call <code> manage.py loaddata filename </code>. Each time you run loaddata, the data will be read from the file and re-loaded into the database. Note this means that if you change one of the rows created by a file and then run loaddata again, you’ll wipe out any changes you’ve made.

##Restore fresh database

    * When you backup whole database by using dumpdata command, it will backup all the database tables

    * If you use this database dump to load the fresh database(in another django project), it can be causes IntegrityError (If you loaddata in same database it works fine)

    * To fix this problem, make sure to backup the database by excluding contenttypes and auth.permissions tables

<code> ./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json </code>

    * Now you can use loaddata command with a fresh database

<code> ./manage.py loaddata db.json </code>
