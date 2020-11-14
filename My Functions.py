class Math:

    @staticmethod
    def sq(x):
        try:
            values = []
            if type(x) == list or type(x) == tuple:
                for num in x:
                    values.append(num**2)
                return values
            
            elif type(x) == int or type(x) == float:
                return x**2

        except TypeError:
            print('Input given is invalid')
            quit()

    @staticmethod
    def sqroot(x):
        try:
            values = []
            if type(x) == list or type(x) == tuple:
                for num in x:
                    values.append(num**0.5)
                return values

            elif type(x) == int or type(x) == float:
                return x**0.5
  
        except TypeError:
            print('Input given is invalid')
            quit()

    @staticmethod
    def raise_to(x, power):
        try:
            values = []
            if type(x) == list or type(x) == tuple:
                for num in x:
                    values.append(num**power)
                return values

            elif type(x) == int or type(x) == float:
                return x**power

        except TypeError:
            print('Input given is invalid')
            quit()

    @staticmethod
    def mean(x):
        try:
            values = 0
            if len(x) <= 1:
                return 'Not enough items given'
            elif type(x) == list or type(x) == tuple:
                for item in x:
                    values += item
                return values / len(x)
        except TypeError:
            print('Input given is invalid')
            quit()

    @staticmethod
    def median(x):
        try:
            value = 0
            if len(x) <= 1:
                return 'Not enough items given'
            elif type(x) == list or type(x) == tuple:
                x = x.sort()
                if len(value) / 2 != 0:
                    index = (len(value) + 1) / 2
                    value = x[index-1]
                    return value
                
                elif len(value) / 2 == 0:
                    index = ((len(value)/2) + (len(value)/2 + 1))/2
                    value = x[index-1]
                    return value
        except TypeError:
            print('Input given is invalid')
            quit()

    @staticmethod
    def mode(x):
        try:
            values = {}
            value = 0
            if len(x) <= 1:
                return 'Not enough items given'
            elif type(x) == list or type(x) == tuple:
                for item in x:
                    values[item] = x.count(item)
                value = max(values, key=values.get)
                return value
        
        except TypeError:
            print('Input given is invalid')
            quit()

    @staticmethod
    def root_to(x, power):
        try:
            values = []
            if type(x) == list or type(x) == tuple:
                for num in x:
                    values.append(num**(1/power))
                return values
            
            elif type(x) == float or type(x) == int:
                return x**(1/power)

        except TypeError:
            print('Invalid Input is given')
            quit()
