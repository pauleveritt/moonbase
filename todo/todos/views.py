from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

import deform
from pyramid_sqlalchemy import Session

from .models import (
    ToDoItem,
    ToDoItemSchema
)


class MyApp:
    def __init__(self, request):
        self.request = request
        self.schema = ToDoItemSchema()
        self.form = deform.Form(self.schema, buttons=('submit',))

    @property
    def this_todo(self):
        id = int(self.request.matchdict['id'])
        return Session.query(ToDoItem).filter_by(id=id).one()

    @view_config(route_name='list', renderer='templates/list.jinja2')
    def list(self):
        todos = Session.query(ToDoItem).order_by(ToDoItem.title)
        return dict(todos=todos)

    @view_config(route_name='add', renderer='templates/add.jinja2',
                 permission='edit')
    def add(self):
        add_form = self.form.render()
        return dict(add_form=add_form)

    @view_config(route_name='add', renderer='templates/add.jinja2',
                 request_method='POST', request_param='submit',
                 permission='edit')
    def add_handler(self):
        controls = self.request.POST.items()
        try:
            appstruct = self.form.validate(controls)
        except deform.ValidationFailure as e:
            # Form is NOT valid
            return dict(add_form=e.render())

        # Valid so add a new ToDoItem to the database, then redirect
        title = appstruct['title']
        Session.add(ToDoItem(title=title))
        todo = Session.query(ToDoItem).filter_by(title=title).one()
        url = self.request.route_url('view', id=todo.id)
        return HTTPFound(url)

    @view_config(route_name='view', renderer='templates/view.jinja2')
    def view(self):
        return dict(todo=self.this_todo)

    @view_config(route_name='edit', renderer='templates/edit.jinja2',
                 permission='edit')
    def edit(self):
        edit_form = self.form.render()
        return dict(edit_form=edit_form)

    @view_config(route_name='edit', renderer='templates/edit.jinja2',
                 request_method='POST', request_param='submit',
                 permission='edit')
    def edit_handler(self):
        controls = self.request.POST.items()
        try:
            appstruct = self.form.validate(controls)
        except deform.ValidationFailure as e:
            # Form is NOT valid
            return dict(add_form=e.render())

        # Valid so add a new ToDoItem to the database, then redirect
        todo = self.this_todo
        todo.title = appstruct['title']
        url = self.request.route_url('view', id=todo.id)
        return HTTPFound(url)

    @view_config(route_name='delete', renderer='templates/delete.jinja2',
                 permission='edit')
    def delete(self):
        todo = self.this_todo
        Session.delete(todo)
        url = self.request.route_url('list')
        return HTTPFound(url)
