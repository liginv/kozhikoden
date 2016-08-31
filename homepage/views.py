from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    output = '''
       <html>
         <head><title>%s</title></head>
         <body>
           <h1>%s</h1><p>%s</p>
         </body>
       </html>
     ''' % (
       'Homepage',
       'Welcome to Kozhikoden',
       'Place for all KOZHIKODENS out their. We are coming!!!'
     )
    return HttpResponse(output)
