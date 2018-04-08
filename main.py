from database import Database
from datetime import datetime
from bottle import route, request, response, template, run, default_app, redirect, static_file

def configure_bottle():
    app = default_app()
    app.config['db'] = Database("items")


@route(method='GET', path='/assets/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='./public')

@route(method='GET', path='/')
def index_page():
    all_items = request.app.config['db'].list_items()
    return template('./templates/index.html', items=all_items)


@route(method='POST', path='/actions/add-item')
def add_item():
    new_item = {
        'name': request.forms.get('name'),
        'location': request.forms.get('location'),
        'added_at': datetime.now()
    }
    request.app.config['db'].add_item(new_item)
    redirect("/")

configure_bottle()
run(host='localhost', port=12345, debug=True)
