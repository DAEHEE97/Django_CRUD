from django.shortcuts import render
from django.shortcuts import HttpResponse

# list_dict
topics = [
     {'id':1, 'title':'routing', 'body':'Routing is ..'},
     {'id':2, 'title':'view', 'body':'View is ..'},
     {'id':3, 'title':'Model', 'body':'Model is ..'},
 ]


# HTML Templeate
def HTMLTemplate(articleTag):
     global topics
     
     ol = ''
     
     for topic in topics:
         ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
     
     return f'''
     <html>
     <body>
         <h1><a href="/">Django</a></h1>
         <ol>
             {ol}
         </ol>
         {articleTag}
     </body>
     </html>
     '''


# Create your views here.

def index(request):
     article = '''
     <h1>h1 tag</h1> 
     Text
     '''
     return HttpResponse(HTMLTemplate(article))


def read(request, id):
     global topics
     
     article = ''
     
     for topic in topics:
         if topic['id'] == int(id):
             article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
     
     return HttpResponse(HTMLTemplate(article))



def create(request, id):
    return HttpResponse('create' + id)


def update(request):
    return HttpResponse('update')

def delete(request):
    return HttpResponse('delete')