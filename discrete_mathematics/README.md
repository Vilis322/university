# ***GENERAL INFO: here are discrete mathematics tasks***

---

## ***DESCRIPTION FOR continued_fraction_converter.py***
+ #### This script converts a rational number into its continued fraction representation using the Euclidean algorithm.

## ***The script consists of the following steps:***
1. #### *Quotient Calculation*
    + perform integer division of the numerator by the denominator to obtain the quotient.
2. #### *Iteration*
    + update the numerator and denominator using the remainder and repeat until the denominator becomes zero.
3. #### *Result*
    + the sequence of quotients forms the continued fraction representation of the given rational number.

## ***REQUIREMENTS***
+ **Python 3.x**

---

## ***DESCRIPTION FOR fermat_prime_check.py***
+ #### This script implements a primality test based on Fermat's factorization method.

## ***The script consists of the following steps:***
1. #### *Validation*
    + if the number is less than 2, it is not prime.
2. #### *Base cases*
    + if the number is 2, it is prime;
    + if the number is even and greater than 2, it is not prime.
3. #### *Fermat's Factorization*
    + check whether the number can be expressed at the difference of two squares.
4. #### *Composite Check*
    + if such a decomposition exists, the number is composite.
    + if no decomposition is found, the number is prime.

## ***REQUIREMENTS***
+ **Python 3.0x**

---

## ***DESCRIPTION FOR gcd_lcm_calculator.py***
+ #### This script calculates the greatest common divisor (GCD) and least common multiple (LCM) of two integers using the Euclidean algorithm.

## ***The script consists of the following steps:***
1. #### *GCD Calculation*
    + uses the Euclidean algorithm to compute the greatest common divisor of two numbers.
2. #### *LCM Calculation*
    + calculates the least common multiple using the formula.
3. #### *Result*
    + prints the GCD and LCM of two given numbers.

## ***REQUIREMENTS***
+ **Python 3.x**

---

## ***DESCRIPTION FOR logical_NOR.py***
+ #### This script generates a truth table for the logical operation "NOR" (NOT OR) for two boolean inputs A and B.

## ***REQUIREMENTS***
+ **Python 3.x**

---

## ***DESCRIPTION FOR prime_checker.py***
+ #### This script checks whether a given number is prime.

## ***The script consists of the following steps:***
1. #### *Initial Validation*
   + the number 2 is prime, while any other even number is not.
2. #### *Divisibility Check*
   + the algorithm checks divisibility only up to the square root of the number;
   + iterates through odd numbers starting from 3, skipping even numbers to improve efficiency;
   + if a divisor is found, the number os not prime.
   
3. #### *Result*
   + the script prints whether the given numbers are prime based on the performed checks.

## ***REQUIREMENTS***
+ **Python 3.x**

---

## ***DESCRIPTION FOR prime_factorization.py***
+ The script finds the prime factorization of a given number using the Sieve of Eratosthenes.

## ***The script consists of the following steps:***
1. #### *Generating Prime Numbers*
   + uses the Sieve of Eratosthenes to generate all prime numbers up to the square root of the given number;
   + marks non-prime numbers by iterating through multiplies of each prime;
   + collects all remaining prime numbers for use in factorization.
2. #### *Factorization Process*
   + iterates through the list of generated prime numbers;
   + repeatedly divides the given number by a prime if it is a factor;
   + appends each prime factor to a list;
   + if the remaining number after division is greater than 1, it is also added as a factor.
3. #### *Result*
   + prints the prime factorization of the given number as a list of prime factors.

## ***REQUIREMENTS***
+ **Python 3.x**

---

## ***DESCRIPTION FOR sheffer_stroke.py****
+ This script generates a truth table for the logical operation "NAND" (NOT AND) for two boolean inputs A and B.

## ***REQUIREMENTS***
+ **Python 3.x**

---

## ***DESCRIPTION FOR sieve_of_eratosthenes.py***
+ This script generates all prime numbers up to a given limit using the Sieve of Eratosthenes algorithm.

## ***The script consists of the following steps:***
1. #### *Initialization*
   + creates a list where each index represents a number, initially marking all as prime;
   + sets 0 and 1 as nin-prime since prime numbers start from 2.
2. #### *Prime Identification*
   + iterates through numbers up to the square root of the limit;
   + if a number is still marked as prime, its multiples are marked as non-prime;
   + this process eliminates nin-prime numbers efficiently.
3. #### *Result*
   + collects all numbers that remain marked as prime;
   + prints the list of prime numbers up to the given limit.

## ***REQUIREMENTS***
+ **Python 3.x**
   