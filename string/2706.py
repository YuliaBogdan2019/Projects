from datetime import datetime

class Person():

    def __init__(self):
        self.__birth_day=datetime.now()
        self.name=None

    def set_name(self,name):
        self.name=name

    def get_name(self):
        return self.name

    def get_birth_day(self):
        return self.__birth_day


class Man(Person):
    __sex='M'

    def __init__(self, name):
        super().__init__()
        self._name=name

    def get_sex(self):
        return self.__sex


class Woman(Person):
    __sex='F'

    def __init__(self, name):
        super().__init__()
        self._name=name

    def get_sex(self):
        return self.__sex


if  __name__=='__main__':
    masha=Woman('masha')
    print(masha.get_name)
    print(masha.get_birth_day)
    vasya=Man('vasya')
    print(vasya.get_name)
    print(vasya.get_birth_day)

    print(masha.get_sex())
    print(vasya.get_sex())
