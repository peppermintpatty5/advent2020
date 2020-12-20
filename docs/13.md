# Day 13

This is the first day where I encountered a problem that I didn't know how to solve. Part 1 was easy, but part 2 seemed impossible.

I have included snippets of LaTeX code in this document. GitHub won't render them, so you'll have to open them in a viewer which does.

**This does not show how to solve the problem, only how to formulate it!**

## Problem

Here is the sample list of bus IDs: `7,13,-,-,59,-,31,19`. The problem is to find the lowest value of `x` such that `(x + 0) % 7 == 0`, `(x + 1) % 13 == 0`, etc.

The missing IDs can be ignored or treated as 1; either way is fine. Recall that dividing by 1 always leaves no remainder, so `x % 1 == 0`.

Here is an ineffective brute-force solution:

```py
>>> x = 0
>>> s = [7, 13, 1, 1, 59, 1, 31, 19]
>>> while not all((x + i) % s[i] == 0 for i in range(len(s))):
...     x += 1
...
>>> x
1068781
```

## Modular Arithmetic

Often you will see mathematicians write "$a$ and $b$ are congruent modulo $n$" which is notated (confusingly) as:

$$a \equiv b \pmod n$$

This is equivalent to saying "$a$ and $b$ differ by $k$ multiples of $n$":

$$\exists k \, (a - b = kn)$$

This can be substituted into the previous code:

```py
>>> congruent = lambda a, b, n: (a - b) % n == 0
>>> x = 0
>>> s = [7, 13, 1, 1, 59, 1, 31, 19]
>>> while not all(congruent(x, -i, s[i]) for i in range(len(s))):
...     x += 1
...
>>> x
1068781
```

Now the problem can be formulated as a system of congruence equations:

$$\begin{aligned}
    x & \equiv 0 \pmod{7}   \\
    x & \equiv -1 \pmod{13} \\
    x & \equiv -4 \pmod{59} \\
    x & \equiv -6 \pmod{31} \\
    x & \equiv -7 \pmod{19}
\end{aligned}$$

## Chinese Remainder Theorem

The Chinese Remainder Theorem can solve a system of $k$ congruence equations in the form $\{x \equiv c_i \pmod{n_i} : 1 \leq i \leq k\}$ if $\{n_1, n_2, \dots, n_k\}$ are pairwise coprime.

Two integers are coprime if their greatest common divisor is 1. Fortunately, our sample and real inputs are pairwise coprime so we can apply the Chinese Remainder Theorem.

That is all the progress I have made. If I have time, I will come back and implement an algorithm for this. In the meantime, I will use one of the many online calculators :)
