# KOZHIKODEN:BACKEND (In Python + Django)
<hr>
###Prerequisites<br>
* Python 2.7 or above (Also works in Pyhton 3.X )
* virtualenv

###Getting started<br>
<code>virtualenv venv</code>
Give the excact name as above to avoid getting it tracked by git.
<code>pip install virtualenv</code>
<code>source venv/bin/activate</code>
**within the virtual Environment run**
<pre><code>pip install -U -r requirements.txt</code></pre>
<code>./manage.py makemigrations</code>
<code>./manage.py migrate</code>
<code>./manage.py loaddata dump/db.json</code>
<code>./manage.py runserver</code>
