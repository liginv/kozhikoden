# KOZHIKODEN:BACKEND (In Python + Django)
**This is the backend part of kozhikoden app**<br>

* [Android app](https://github.com/alenthomas/kozhikoden-react-native)
* [iOS app](https://github.com/liginv/kozhikoden-ios)

###Prerequisites<br>
* Python 2.7 or above (Also works in Pyhton 3.X )
* virtualenv

###Getting started<br>
Create a Virtual Environment.**Give the exact name(venv) for the virtual enviroment.**<br>
<pre><code>$ virtualenv venv</code></pre>


<pre><code>$ source venv/bin/activate</code></pre><br>

####Inside the virtual Environment run the following commands in order:<br>

This will install the dependencies into the virtual environment.
<pre><code>$ pip install -U -r requirements.txt</code></pre><br>
This will build the models(database)
<pre><code>$ ./manage.py makemigrations</code></pre><br>
This will implement the models into sqlite
<pre><code>$ ./manage.py migrate</code></pre><br>
This will load the dummy datas into the db
<pre><code>$ ./manage.py loaddata dump/db.json</code></pre><br>
This creates  a local server to run the application
<pre><code>$ ./manage.py runserver</code></pre>

<p align="center">
  <b>Made with ♥ by Kozhikodens</b><br>
</p>
