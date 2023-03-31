# Level 1. A floating-point underflow vulnerability

In `hack.py`, the attacker tricked the system by supplying an extremely high amount as a fake payment,
immediately followed by a payment reversal. The exploit passes a huge number, causing an underflow while subtracting the cost of purchased items, resulting in a zero net.

It's a good practice to limit your system input to an acceptable range instead of accepting any value.

We also need to protect from a scenario where the attacker sends a huge number of items, resulting in
a huge net. We can do this by limiting all variables to reasonable values.
