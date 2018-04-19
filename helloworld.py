from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval
from trytond import backend

__all__ = ['Country', 'Subdivision', 'Zip']


class HelloWorld(ModelSQL, ModelView):
    'Hello World'
    __name__ = 'hello.world'
    name = fields.Char('Hello', required=True)
