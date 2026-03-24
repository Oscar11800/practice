# Lecture Notes Monday 3-23

## Introduction
- what is a problem: a function 
    - ex. f: input -> output
    - mathematically, functions are pairs of inputs and outputs
        - decision problems: outputs y/n or T/F for all inputs
        - all computational representaiton of data is going to become some sequence of bits, symbols, text to be processed by the computer (ie. all inputs are strings)
        - The "problem" can be described as {x in Strings | f(x) = yes}
            - problems can be described as a set of strings
            - sets of strings are called "languages"
            - computation is just processing input strings and thinking about problems as sets of strings
    - solutions are algorithms that computes the function
- what is an alphabet: finite set where we define our symbols
    - ex: {a, b, c, ..., z}, {0, 1}, {A, C, G, T}
    - denoted by $\Sigma$
- Strings: sequence of symbols drawn from some alphabet
    - denoted by $w = a_1a_2 ... a_n, a_i \in $\Sigma$
    - $\epsilon$ is the empty string
    - ex: $a_x, a \in \Sigma, x$ is a string
    - strings are recursive object that can be recursed
    - Concatenation
        - definition: $u = a_1a_2 ... a_m , v = b_1b_2 ... b_n$, $u\cdot v = a_1 ... a_mb_1 ... b_n$
        - associative s.t. u(vw) = (uv)w
        - identity: if $u = \epsilon, uv = v$
        - if $u = ax, uv = a(x\cdotv)
            - ex. $cat \cdot hat = c(at \cdot hat) = c(a(t\cdot hat)) = c(a(t(\epsilon \cdot hat))) = c(a(that)) = c(athat)) = cathat


## Questions
- Why represent concatenation with multiplication instead of addition?
- 

