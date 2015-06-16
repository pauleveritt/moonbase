from pyramid.httpexceptions import HTTPFound
from pyramid.security import (
    remember,
    forget,
)
from pyramid.view import (
    view_config,
    forbidden_view_config
)


from . import USERS


class MyApp:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid

    @view_config(route_name='login',
                 renderer='templates/login.jinja2')
    @forbidden_view_config(renderer='templates/login.jinja2')
    def login(self):
        request = self.request
        login_url = request.route_url('login')
        referrer = request.url
        if referrer == login_url:
            referrer = '/'  # never use login form itself as came_from
        came_from = request.params.get('came_from', referrer)
        message = ''
        login = ''
        password = ''
        if 'form.submitted' in request.params:
            login = request.params['login']
            password = request.params['password']
            if USERS.get(login) == password:
                headers = remember(request, login)
                return HTTPFound(location=came_from,
                                 headers=headers)
            message = 'Failed login'

        return dict(
            name='Login',
            message=message,
            url=request.application_url + '/login',
            came_from=came_from,
            login=login,
            password=password,
        )

    @view_config(route_name='logout')
    def logout(self):
        headers = forget(self.request)
        url = self.request.route_url('list')
        return HTTPFound(location=url, headers=headers)
