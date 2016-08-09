#Loading data
 just call <code>manage.py loaddata filename <code>. Each time you run loaddata, the data will be read from the file and re-loaded into the database. Note this means that if you change one of the rows created by a file and then run loaddata again, you’ll wipe out any changes you’ve made.
