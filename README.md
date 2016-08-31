# KOZHIKODEN:BACKEND (In Python + Django)
###Prerequisites<br>
* Python 2.7 or above (Also works in Pyhton 3.X )
* virtualenv

###Getting started<br>
Create a Virtual Environment
<pre><code>virtualenv venv</code></pre>
Give the excact name as above to avoid getting it tracked by git.
</pre><code>source venv/bin/activate</code></pre>
Within the virtual Environment run
<pre><code>pip install -U -r requirements.txt <br>
./manage.py makemigrations <br>
./manage.py migrate <br>
./manage.py loaddata dump/db.json <br>
./manage.py runserver</code></pre>
