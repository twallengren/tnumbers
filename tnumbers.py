EVEN = 'EVEN'
ODD = 'ODD'

################################################################################
################################################################################

class Zero():
    '''
    Abstract zero class. Reflects properties of zero without direct references
    to zero.
    '''

    def plus(self, other):
        '''
        Zero is the additive identity.
        '''

        return other

    def parity(self):
        '''
        Zero is an even number.
        '''

        return EVEN

    def __repr__(self):
        '''
        How to display this class to the shell.
        '''

        return 'Zero'

    def __eq__(self, other):
        '''
        Define equality if displayed to shell equivalently.
        '''

        return repr(self) == repr(other)

################################################################################
################################################################################

class One():
    '''
    Abstract one class. Reflects properties of one without direct references
    to one.
    '''

    def plus(self, other):
        '''
        Adding 1 returns the successor of other.
        '''

        return create_successor(other)

    def parity(self):
        '''
        One is an odd number.
        '''

        return ODD

    def __repr__(self):
        '''
        How to display this class to the shell.
        '''

        return 'One'

    def __eq__(self, other):
        '''
        Define equality if displayed to shell equivalently.
        '''

        return repr(self) == repr(other)

################################################################################
################################################################################

class AbstractBinary():
    '''
    Abstract Binary class. Used to construct all numbers from Zero() and One().

    Input a list of digits of the above zero and one class. ie to create an
    AbstractBinary instance of the number four, you would write:

    four = AbstractBinary([Zero(), Zero(), One()])

    note that the input is backwards (binary would normally go right to left)
    but it will still display as expected ie:

    repr(four) = [AbOne, AbZero, AbZero]
    
    '''

    def __init__(self, digits):

        self.digits = digits

    def __repr__(self):

        return str(self.digits[::-1])

    def __plus__(self, other):

        pass

    def __eq__(self, other):

        if len(self.digits) != len(other.digits):

            return False

        else:

            return all([self.digits[index] == other.digits[index] for index in range(len(self.digits))])

    def parity(self):

        return EVEN if isinstance(self.digits[0], Zero) else ODD

################################################################################
################################################################################

def create_successor(abstract_number):

    if isinstance(abstract_number, Zero):

        return One()

    elif isinstance(abstract_number, One):

        return AbstractBinary([Zero(), One()])

    else:

        newdigits = list(abstract_number.digits)

        for index,digit in enumerate(abstract_number.digits):

            if isinstance(digit, Zero):

                newdigits[index] = One()

                break

            else:

                newdigits[index] = Zero()

        if all([digit == Zero() for digit in newdigits]):

            newdigits.append(One())

        return AbstractBinary(newdigits)

            
