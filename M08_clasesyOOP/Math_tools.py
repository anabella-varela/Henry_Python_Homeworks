class Math:
    def __init__(self, list_data):
        self.list= list_data
        '''
        Math allows to perform several fuctions from an imported list 
        '''
        
    def __Primo (self, n):#private method for calculation. Recieves a number n
        ''' 
        Function that informs if a number is a prime number (True) or not (False)
        '''
        is_prime= True
        for div in (range (2, n)):
            if (n % div) == 0:
                is_prime= False
                break
        return is_prime
    
    def Primo (self):
        for n in self.list:
            if self.__Primo(n):
                print (f'{n} is a Prime number')
            else:
                print (f'{n} is a Complex number')

    def Moda (self):
        '''
        returns the mode and number of repetitios from a list
        '''
        counts = {} #create an empty dictionary
        list = self.list
        for num in list:
            if num in counts:
                counts[num] += 1 #I will increse the value of the num Key in one digit
            else:
                counts[num] = 1 #I will insert the numas a key, and the 1 as a value

        mode = max(counts, key=counts.get) #key=counts.get is used to compare the elements of the counts dictionary based on their corresponding values (repetition counts).
        # I find the element with the max count
        repetitions = counts[mode]

        return mode, repetitions
    
          
        
    def __Temp_convertor (self, value, inp, outp): #here I calculate the conversion. This is a private method, indicated by the double underscore prefix (__).
            '''
            converts temperatures values for C (celsius), F (farenheit), and K(kelvin)
            '''
            temp = 0  # Initialize temp with a default value. This will prevent the UnboundLocalError.
            if inp == 'C':
                    if outp == 'C':
                        temp = value
                    elif outp == 'F':
                        temp = (value * 9/5) + 32
                    elif outp == 'K':
                        temp = value + 273.15
                        
            if inp == 'F':
                if outp == 'F':
                    temp = value
                elif outp == 'C':
                    temp = (value - 32) * 5/9
                elif outp == 'K':
                    temp = (value -32) * 5/9 + 273.15

            if inp == 'K':
                if outp == 'K':
                    temp = value
                if outp == 'C':
                    temp = value - 273.15
                elif outp == 'F':
                    temp = ((value - 273.15) * 9/5) +32

            return temp
    
    def Temp_convertor (self, inp, outp): # is a public method, accessible from outside the class,
        for value in self.list:  #here I iterate value from the list
            print(value, inp, 'equals to', self.__Temp_convertor(value, inp, outp), outp)


      
    def __Factorial (self, n):
        f = 1 
        initial_n = n #store the initial value so I can call it later
        if type(n) != int or n < 0:
            print (f'{n} is not a valid number. Enter a positive natural number')
            return None
        elif isinstance (n, int):
            while n > 0:
                f = f * n
                n -= 1 
            return f
        else:
            return None
        
    def Factorial (self):
        for n in self.list:
            print('The factorial of', n, 'is', self.__Factorial(n))