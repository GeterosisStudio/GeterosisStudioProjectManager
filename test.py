
class ClsBase(object):
    def __init__(self):
        pass

class ClsOne(ClsBase):
    def __init__(self):
        pass

class ClsTwo(ClsOne):
    def __init__(self):
        pass

class ClsThree(ClsTwo):
    def __init__(self):
        pass

class ClsSas(ClsOne):
    def __init__(self):
        pass


class ClsAssa(ClsOne):
    def __init__(self):
        pass

qq = ClsAssa()

bb = list(reversed(ClsAssa().__class__.mro()))[1:]

print bb
print issubclass(type(qq), ClsBase)
