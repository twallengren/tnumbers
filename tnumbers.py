EVEN = 'EVEN'
ODD = 'ODD'

################################################################################
################################################################################

class Zero():
    '''
    Abstract zero class. Reflects properties of zero without direct references
    to zero.
    '''

    ############################################################################

    def parity(self):
        '''
        Zero is an even number.
        '''

        return EVEN

    ############################################################################

    def __repr__(self):
        '''
        How to display this class to the shell.
        '''

        return 'Zero'

    ############################################################################

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

    ############################################################################

    def parity(self):
        '''
        One is an odd number.
        '''

        return ODD

    ############################################################################

    def __repr__(self):
        '''
        How to display this class to the shell.
        '''

        return 'One'

    ############################################################################

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

    four = AbstractBinary([One(), Zero(), Zero()])
    '''

    ############################################################################

    def __init__(self, digits):
        '''
        Initialize abstract binary. Set digit list on self.
        '''

        # list is reversed to optimize speed
        # it is faster to append to end of list than push to front
        self.digits = digits[::-1]

    ############################################################################

    def __repr__(self):
        '''
        Show digit list in reverse in shell.
        '''

        return str(self.digits[::-1])

    ############################################################################

    def __len__(self):

        return len(self.digits)

    ############################################################################

    def __add__(self, other):
        '''
        Define behavior of the + operator for abstract binary numbers.
        '''

        return AbstractBinary(self.add_digit_lists(self.digits, other.digits)[::-1])

    ############################################################################

    def __mul__(self, other):
        '''
        Define behavior of the * operator for abstract binary numbers.
        '''

        count = AbstractBinary([One()])
        product = AbstractBinary(self.digits[::-1])

        while count != other:

            product = product + AbstractBinary(self.digits[::-1])
            count = count.successor()

        return product

    ############################################################################

    def __eq__(self, other):
        '''
        Define equality for abstract binary numbers.
        1) digit list must be same length
        2) digits must be equivalent one for one between the lists
        '''

        if len(self) != len(other):

            return False

        else:

            return all([self.digits[index] == other.digits[index] for index in range(len(self.digits))])

    ############################################################################

    def parity(self):
        '''
        Number is even if first digit is 0, odd otherwise.
        '''

        return EVEN if isinstance(self.digits[0], Zero) else ODD

    ############################################################################

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

        return AbstractBinary(newdigits[::-1])

    ############################################################################

    def add_digit_lists(self, digitlist1, digitlist2):
        '''
        Function to add binary digit lists. Used in the __add__ method.
        '''

        carrylist = [Zero()]
        sumlist = []

        if len(digitlist1) < len(digitlist2):

            shortlist = digitlist1
            longlist = digitlist2

        else:

            shortlist = digitlist2
            longlist = digitlist1

        for index,digit in enumerate(shortlist):

            otherdigit = longlist[index]

            if isinstance(digit,Zero):

                sumlist.append(otherdigit)
                carrylist.append(Zero())

                continue

            if isinstance(otherdigit,Zero):

                sumlist.append(digit)
                carrylist.append(Zero())

                continue

            sumlist.append(Zero())
            carrylist.append(One())

        while index < len(longlist) - 1:

            index = index + 1

            sumlist.append(longlist[index])

        if all([isinstance(carried,Zero) for carried in carrylist]):

            return sumlist

        return self.add_digit_lists(sumlist, carrylist)

    ############################################################################

    def native(self):
        '''
        Method to translate abstract binary to python int.
        '''

        native = 0

        for index,digit in enumerate(self.digits):

            if isinstance(digit,One):

                native = native + 2**index

        return native

################################################################################
################################################################################

            
