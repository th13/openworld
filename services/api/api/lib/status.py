### status.py
### 
### Contains Flask view function decorators for common HTTP status codes that 
### can be standardized across the API.

from functools import wraps

status_codes = [
    {
        'name': 'ok',
        'code': 200,
        'message': 'The request was processed.'
    },
    {
        'name': 'forbidden',
        'code': 403,
        'message': 'This resource is forbidden.'
    },
    {
        'name': 'not_found',
        'code': 404,
        'message': 'This resource could not be found. Maybe you mispelled it?'
    },
    {
        'name': 'im_a_teapot',
        'code': 418,
        'message': 'http://www.youtube.com/watch?v=e69-GO4bYLM'
    },
    {
        'name': 'not_implemented',
        'code': 501,
        'message': 'This functionality has not been implemented yet.'
    }
]

to_create = ''

for status_code in status_codes:
    to_create += '''
{1} = {0[code]}
def {0[name]}(route_fn):
    @wraps(route_fn)
    def decorated(*args, **kwargs):
        return '{0[message]}', {1}
    return decorated
'''

    to_create = to_create.format(status_code, status_code['name'].upper())

exec(to_create)