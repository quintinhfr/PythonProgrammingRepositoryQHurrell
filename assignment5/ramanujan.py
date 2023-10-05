
import stdio
import sys
    
# NOTE: the vast majority of this program is from the booksite, specifically the link (https://introcs.cs.princeton.edu/python/13flow/ramanujanfor.py.html), as I could not get this program working on my own.

#this is the command line argument that sets the ceiling for numbers that are processed

n = int(sys.argv[1])

#When I originally tried this, I couldn't get the for loops to stop whenver they needed to check the next variable, I now understand the range system and how that must play out.

for a in range(1, n+1):
    a3 = a*a*a
    if (a3 > n):
        break


    for b in range(a, n+1):
        b3 = (b*b*b)
        if a3 + b3 > n:
            break;

   
        for c in range(a+1, n+1):
            c3 = c*c*c
            if (c3 > a3 + b3):
                break

          
            for d in range(c, n+1):
                d3 = d*d*d
                if (c3 + d3 > a3 + b3):
                    break

                if c3 + d3 == a3 + b3:
                    
                    stdio.write(str(a) + '^3 + ' + str(b) + '^3 = ')
                    stdio.write(str(c) + '^3 + ' + str(d) + '^3')
                    stdio.write(" = ")
                    stdio.write(str(a3+b3))
                    stdio.writeln()

