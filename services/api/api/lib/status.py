### status.py
### 
### Contains Flask view function decorators for common HTTP status codes that 
### can be standardized across the API.

from functools import wraps

## -- Status code definitions --
OK = 200
FORBIDDEN = 403
NOT_FOUND = 404
IM_A_TEAPOT = 418
NOT_IMPLEMENTED = 501


## -- Custom status code view functions --

def not_implemented(route_fn):
    """Flask route decorator for routes that haven't been implemented yet."""
    @wraps(route_fn)
    def decorated(*args, **kwargs):
        return 'This functionality has not been implemented yet.', NOT_IMPLEMENTED
    return decorated

def not_found(route_fn):
    """Flask route decorator for routes that don't seem to exist."""
    @wraps(route_fn)
    def decorated(*args, **kwargs):
        return 'This resource could not be found. Maybe you mispelled it?', NOT_FOUND
    return decorated

def forbidden(route_fn):
    """Flask route decorator for forbidden requests."""
    @wraps(route_fn)
    def decorated(*args, **kwargs):
        return 'This resource is forbiden.', FORBIDDEN
    return decorated

# This one is an easter egg.
def im_a_teapot(route_fn):
    @wraps(route_fn)
    def decorated(*args, **kwargs):
        return 'http://www.youtube.com/watch?v=e69-GO4bYLM', IM_A_TEAPOT
    return decorated