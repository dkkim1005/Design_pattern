#!/usr/bin/python2.7

class abstract_factory:
    def __init__(self):    
        print "Let's start abstract factory!"
    
    def create(self,sth_type):
        raise NotImplemented


class Vegetable_factory(abstract_factory):
    def __init__(self):
        abstract_factory.__init__(self)
        print "Now, vegetable factory is operating."

    def create(self,vegetable_type):
        assert type(vegetable_type) == str 
        if(vegetable_type == 'Tomato'):
            return Tomato()
        else: 
            raise KeyError('There are no options.')


class Vegetable:
    def __init__(self):
        print "Vegetable is good for our health."
    
    def taste(self):
        raise NotImplemented

class Tomato(Vegetable):
    def __init__(self):
        Vegetable.__init__(self)
        print "Tomato is subset of vegetable."

    def taste(self):
        print "Tomato has sour and sweet tastes."


#Mimicing abstract class with 'NotImplemeted' construction.
#Fruit : Base class
class Fruit:
    def __init__(self):
        print "Fruit is yammy."

    def taste(self):
        raise NotImplemented

#Apple : derived class
class Apple(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print "Apple is subset of fruit."
    
    def taste(self):
       print "Apple has sweet taste."

#Lemon : derived class
class Lemon(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print "Lemon it subset of fruit"

    def taste(self):
        print "Lemon has sour taste"

#Creating each instance encapsulizely with using factory.
class Fruit_factory(abstract_factory):
    def __init__(self):
        abstract_factory.__init__(self)
        print "Now, fruit factory is operating."

    def create(self,fruit_type):
        assert type(fruit_type) == str
        if(fruit_type == 'Apple'):
            return Apple()
        elif(fruit_type == 'Lemon'):
            return Lemon()
        else:
            raise KeyError('There are no options.')


factory = Fruit_factory()
lemon = factory.create('Lemon')
apple = factory.create('Apple')
factory = Vegetable_factory()
tomato = factory.create('Tomato')
                                            


