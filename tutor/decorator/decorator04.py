class decoclass(object):

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        # before f actions
        print ('decorator initialised')
        self.f(*args, **kwargs)
        print( 'decorator terminated')
        # after f actions

@decoclass
def klass():
    print('class')

klass()