'''
Suppose that you’d like to implement a cookie jar in which to store cookies. In a file called jar.py, 
implement a class called Jar with these methods:

__init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit 
in the cookie jar. If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.

__str__ should return a str with  🍪, where  is the number of cookies in the cookie jar. 
For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"

deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, 
deposit should instead raise a ValueError.

withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, 
though, withdraw should instead raise a ValueError.

capacity should return the cookie jars capacity.

size should return the number of cookies actually in the cookie jar.
'''

class Jar:
    def __init__(self, size, capacity=12):
        self.size = size
        self.capacity = capacity

    def __str__(self):
        return '🍪'

    def deposit(self, n):
        if (self.size + n) > 12:
            raise ValueError
        else:
            self.size += n

    def withdraw(self, n):
        if self.size == 0:
            raise ValueError
        elif self.size - n < 0:
            raise ValueError
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size

def main():
    cookies = Jar(0, 12)
    cookies.deposit(3)
    print(f"{cookies}")

if __name__ == "__main__":
    main()