import sys

def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    # s = list(range(n))
    # for i in range(n):
    #     s[i] = str(s[i]+1)
    #     if int(s[i])%5 == 0 and int(s[i])%3 == 0:
    #         s[i] = 'FizzBuzz'
    #     elif int(s[i])%3 == 0:
    #         s[i] = 'Fizz'
    #     elif int(s[i])%5 == 0:
    #         s[i] = 'Buzz'
    # return s

    # return [(i%3==0)*"Fizz" + (i%5==0)*"Buzz" or str(i) for i in range(1, n+1)]
    
    return [('Fizz' if i % 3 == 0 else '') + ('Buzz' if i % 5 == 0 else '') + (str(i) if not (i % 3 == 0 or i % 5 == 0) else '') for i in range(1,n+1)]
    
print(fizzBuzz(2))
