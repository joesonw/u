from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from django.utils import simplejson as _j

@dajaxice_register
def test(request):
    return _j.dumps({'message':'Hello World'})

@dajaxice_register(method='GET')
def test2(request):
    dajax = Dajax()
    dajax.alert('hello world 2') ;
    return dajax.json()
    