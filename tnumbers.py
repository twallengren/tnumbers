EVEN = 'EVEN'
ODD = 'ODD'

################################################################################
################################################################################

class Zero():
    '''
    Abstract zero class. Reflects properties of zero without direct references
    to zero.
    '''

    def __add__(self, other):
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

    def __add__(self, other):
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

    this is done because it is quicker to append to the end of the list than
    it is to push something to the beginning of the list.
    '''

    def __init__(self, digits):
        '''
        Initialize abstract binary. Set digit list on self.
        '''

        self.digits = digits

    def __repr__(self):
        '''
        Show digit list in reverse in shell.
        '''

        return str(self.digits[::-1])

    def __add__(self, other):

        pass

    def __eq__(self, other):
        '''
        Define equality for abstract binary numbers.
        1) digit list must be same length
        2) digits must be equivalent one for one between the lists
        '''

        if len(self.digits) != len(other.digits):

            return False

        else:

            return all([self.digits[index] == other.digits[index] for index in range(len(self.digits))])

    def parity(self):
        '''
        Number is even if first digit is 0, odd otherwise.
        '''

        return EVEN if isinstance(self.digits[0], Zero) else ODD

    def successor(self):
        '''
        Return successor of Abstract Binary.
        '''

        newdigits = list(self.digits)

        for index,digit in enumerate(self.digits):

            if isinstance(digit, Zero):

                newdigits[index] = One()

                break

            else:

                newdigits[index] = Zero()

        if all([digit == Zero() for digit in newdigits]):

            newdigits.append(One())

        return AbstractBinary(newdigits)

################################################################################
################################################################################

            
