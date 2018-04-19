from trytond.pool import Pool

from .helloworld import HelloWorld


def register():
    Pool.register(
        HelloWorld,
        module='helloworld', type_='model'
    )
