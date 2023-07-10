from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

from django.views.decorators.csrf import csrf_exempt


next_id = 4

# list_dict
topics = [
     {'id':1, 'title':'routing', 'body':'Routing is ..'},
     {'id':2, 'title':'view', 'body':'View is ..'},
     {'id':3, 'title':'Model', 'body':'Model is ..'},
 ]


# HTML Templeate
#  홈 id = None

def HTMLTemplate(articleTag, id = None):
     global topics
     
     # id 값이 존재하면 delete 처리 
     contextUI = ''

     if id != None:
         contextUI = f'''
            <li>
                <form action="/delete/" method="post">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value="delete">
                </form>
            </li>

         '''
         

     ol = ''
     
     for topic in topics:
         ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
     
     return f'''
     <html>
     <body>
         <h1><a href="/">Created by HTMLTemplate</a></h1>
         <ul>
             {ol}
         </ul>
         {articleTag}
         <ul>
            <li><a href="/create/">create</a></li>
            {contextUI}
            
        </ul>
     </body>
     </html>
     '''


# Create your views here.

def index(request):
     article = '''
     <h2>def index</h2> 
     Text ...
     '''
     return HttpResponse(HTMLTemplate(article))


def read(request, id):
     global topics
     
     article = ''
     
     for topic in topics:
         if topic['id'] == int(id):
             article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
     
     return HttpResponse(HTMLTemplate(article, id))


@csrf_exempt
def create(request):
    global next_id

    if request.method == 'GET':
        article = '''
            <form action="/create/" method ="post">
                <p><input type = "text" name = "title" placeholder = "title"></p>
                
                <p><textarea name = "body" placeholder = "body"></textarea></p>
                
                <p><input type = "submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    
    elif request.method == 'POST':
        
        title = request.POST['title']
        body = request.POST['body']
        
        newTopic = {"id":next_id, "title":title, "body":body}
        topics.append(newTopic)
       
        url = '/read/'+str(next_id)
       
        next_id = next_id + 1
        
        return redirect(url)


@csrf_exempt
def delete(request):
    global topics
    
    if request.method == 'POST':
        id = request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        
        return redirect('/') 
    


def update(request):
    return HttpResponse('update')