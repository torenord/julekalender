def prime(n):
    return all(n % i != 0 for i in range(2, int(n**0.5)+1))

def reverse(n):
    return int(str(n)[::-1])

def palindrome(n):
    return n == reverse(n)

print sum(prime(i) and prime(reverse(i)) and not palindrome(i) for i in range(1, 1000))
