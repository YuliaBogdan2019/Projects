class AClass():
    name='Vasya'

def __getattr__(self, name):
    pass
    super()getattr__(name)
    #return self.__dict__.get(name)
    try:
        value=self.__dict__(name)
    except KeyError:
        raise AtributError ('Atribut '{name}' not found)
    else:
        return self, __dict__(name)


#def __len__(self)
#    return 5

def __bytes__(self): #preobrazovat v bity
    return bytes(4)


def __call__(self, name, *args, **kwargs):
    return name


def __iter__(self):
    self.data=[1,1,2,3]
    self.index=0
    return self

def __next__(self):
    result=self.data[self.index]
    self.index==1
    return result

def 





if __name__=='__main__':
    a=AClass('A', 'Object')
    b=AClass('B', 'Object')
    a.attr1=1
    #print(a.attr1)
    #print(b.attr2)
    print(len(a))
    print(bytes(a))
    data=[2,4,5]
    el=4
    if el in data:
        print(el)
    else:
        print('Error')
