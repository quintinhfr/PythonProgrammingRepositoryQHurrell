#---------------
# stresstest.py
#---------------

import integers
import stdio
import random



#picks random perameters

a = random.randint(2,100000000)
b = random.randint(2, 1000000000)


stdio.writeln("------------")
stdio.writeln("isprime Stress Test")
stdio.writeln(integers.isprime(a))
stdio.writeln("------------")

stdio.writeln()
stdio.writeln()

a = random.randint(2,100000000)
b = random.randint(2, 100000000)

stdio.writeln("------------")
stdio.writeln("isrelativeprime Stress Test")
stdio.writeln(integers.isrelativeprime(a, b))
stdio.writeln("------------")

stdio.writeln()
stdio.writeln()

a = random.randint(2,100000000)
b = random.randint(2, 100000000)

stdio.writeln("------------")
stdio.writeln("factors Stress Test")
stdio.writeln(integers.factors(a))
stdio.writeln("------------")

stdio.writeln()
stdio.writeln()

a = random.randint(2,1000000)
b = random.randint(2, 1000000)

stdio.writeln("------------")
stdio.writeln("divisor Stress Test")
stdio.writeln(integers.divisor(a, b))
stdio.writeln("------------")

stdio.writeln()
stdio.writeln()

#NOTE ---- Multiple has to work with much less large numbers due to its runtime

a = random.randint(2,10000)
b = random.randint(2, 10000)

stdio.writeln("------------")
stdio.writeln("multiple Stress Test")
stdio.writeln(integers.multiple(a, b))
stdio.writeln("------------")

stdio.writeln()
stdio.writeln()

a = random.randint(2,1000000)
b = random.randint(2, 1000000)

stdio.writeln("------------")
stdio.writeln("totient Stress Test")
stdio.writeln(integers.totient(a))
stdio.writeln("------------")

stdio.writeln()
stdio.writeln()

a = random.randint(2,10000000000000)
b = random.randint(2, 100000000000)


stdio.writeln("------------")
stdio.writeln("isodd Stress Test")
stdio.writeln(integers.isodd(a))
stdio.writeln("------------")

stdio.writeln()
stdio.writeln()

a = random.randint(2,10000000000000)
b = random.randint(2, 100000000000)

stdio.writeln("------------")
stdio.writeln("iseven Stress Test")
stdio.writeln(integers.iseven(a))
stdio.writeln("------------")

stdio.writeln()
stdio.writeln()





