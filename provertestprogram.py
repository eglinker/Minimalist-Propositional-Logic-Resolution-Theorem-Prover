
# provertestprogram.py, version 1.0.0, April 30, 2017
# 
# DESCRIPTION
#
# Test program for the Minimalist Propositional Logic Resolution 
# (Theorem) Prover contained in: PLResolutionProver.py
#
# LICENCE
#
# This file is part of minimalist propositional logic resolution prover.
# It may be used for free under the terms of the licence below:
#
# Copyright (c) 2013 by Erich Glinker.  
# All Rights Reserved Worldwide.
# 
# By using this source code you agree to the following terms:
#
#	a)	You are permitted to use this source code for personal 
#		and/or commercial purposes.
#	b)	You may redistribute this text as part of a project 
#		ONLY IF this legal agreement remains, and any 
#		changes/additions to the text or documentation are 
#		clearly marked.
#	c)	This source code is provided "as is", with NO WARRANTY of 
#		any kind, express or implied, not even "fitness for 
#		a particular purpose".
#	d)	Erich Glinker shall not be held liable under any 
#		circumstances for any damage resulting from the use 
#		or misuse of this source code.
#	e)	In jurisdictions where any part of this legal agreement 
#		is not legal or not enforceable by law, part 'e' shall 
#		remain upheld, and you are expressly forbidden to use 
#		this text for any purpose.


#Load requires modules 
import PLResolutionProver
import time


# Instantiate a solver.
myEngine =  PLResolutionProver.PLResolutionProver()

print "#######################################################"
print "#######################################################"
print "#######################################################"


print "#######################################################"
print "test case #1, Modus Ponens"
print "A implies B, A is True, therfore B is true"
# note: A = 1, B = 2, not A = -1	
# https://en.wikipedia.org/wiki/Modus_ponens

#	Empty knowlegebase by setting KB to empty list.
myEngine.setKB([])

#	Add 'A implies B' to the knowlege base.
myEngine.addToKB([-1,2])
 
#	Add A to knowlgebase and Resolve. 
myEngine.addToKBAndResolve([1])  	

#	Look at resulting knowlegebase (KB).
print myEngine.getKB()
print


print "#######################################################"
print "test case #2, Modus Tollens"
print "A implies B, not B, therfore not A"
# note: A = 1, B = 2, not B = -2	

#	Empty knowlegebase by setting KB to empty list.
myEngine.setKB([])

#	Add 'A implies B' to the knowlege base.
myEngine.addToKB([-1,2])
 
#	Add '~B' to knowlgebase and Resolve. 
myEngine.addToKBAndResolve([-2])  	

#	Look at resulting knowlegebase (KB).
print myEngine.getKB()
print


print "#######################################################"
print "test case #3, Hypothetical Syllogism"
print "A implies B, B implies C, therfore A implies C"
# note: A = 1, not A = -1, B = 2, not B = -2	
#		C = 3, not C = -3

#	Empty knowlegebase by setting KB to empty list.
myEngine.setKB([])

#	Add 'A implies B' to the knowlege base.
myEngine.addToKB([-1,2])
 
#	Add 'B implies C' to knowlgebase and Resolve. 
myEngine.addToKBAndResolve([-2,3])  	

#	Look at resulting knowlegebase (KB).
print myEngine.getKB()
print


print "#######################################################"
print "test case #4"
print "A -> B, B -> C, ~C, Therefore A - > C, ~C"
print "(resolves all clauses as added with all relevent clauses.)"
# note: A = 1, not A = -1, B = 2, not B = -2	
#		C = 3, not C = -3

#	Empty knowlegebase and set KB to first clause list.
myEngine.setKB([])

#	Add 'A implies B' to the knowlege base.
myEngine.addToKB([-1,2])
 
#	Add 'B implies B' to knowlgebase and Resolve. 
myEngine.addToKBAndResolve([-2,3])

#	Add '~C' to knowlgebase and Resolve. 
myEngine.addToKBAndResolve([-3])    	

#	Look at resulting knowlegebase (KB).
print myEngine.getKB()
print


print "#######################################################"
print "test case #5, "
print "A -> B, B -> C, ~C, Therefore ~B, ~A"
print "(resolve only last clause and resulting clauses.)"
# note: A = 1, not A = -1, B = 2, not B = -2	
#		C = 3, not C = -3

#	Empty knowlegebase and set KB to first clause list.
myEngine.setKB([])

#	Add 'A implies B' to the knowlege base.
myEngine.addToKB([-1,2])
 
#	Add 'B implies C' to knowlgebase 
myEngine.addToKB([-2,3])

#	Add '~c' to knowlgebase and Resolve. 
myEngine.addToKBAndResolve([-3])    	

#	Look at resulting knowlegebase (KB).
print myEngine.getKB()
print


print "#######################################################"
print "test case #6"
print "A -> B, B -> C, A, Therefore C"
print "(resolves all clauses as added with all relevent clauses.)"

# note: A = 1, not A = -1, B = 2, not B = -2	
#		C = 3, not C = -3

#	Empty knowlegebase and set KB to first clause list.
myEngine.setKB([])

#	Add 'A implies B' to the knowlege base.
myEngine.addToKB([-1,2])
 
#	Add B implies C to knowlgebase and Resolve. 
myEngine.addToKBAndResolve([-2,3])

#	Add A to knowlgebase and Resolve. 
myEngine.addToKBAndResolve([1])    	

#	Look at resulting knowlegebase (KB).
print myEngine.getKB()
print


print "#######################################################"
print "test case #7, "
print "A -> B, B -> C, A, Therefore C"
print "(resolve only last new clause and resulting clauses.)"
# note: A = 1, not A = -1, B = 2, not B = -2	
#		C = 3, not C = -3

#	Empty knowlegebase and set KB to first clause list.
myEngine.setKB([])

#	Add 'A implies B' to the knowlege base.
myEngine.addToKB([-1,2])
 
#	Add A implies B to knowlgebase 
myEngine.addToKB([-2,3])

#	Add A to knowlgebase and Resolve. 
myEngine.addToKBAndResolve([1])    	

#	Look at resulting knowlegebase (KB).
print myEngine.getKB()
print


print "#######################################################"
print "test case #8, C =  A and B, ~C, A, therefore ~B"
print "A and B -> C, ~A -> ~C, ~B -> ~C, ~C, A, therefore ~B"  
print "(resolves all clauses as added with all relevent clauses.)"
#
#	-1 or -2 or 3
#	1 or -3
#	2 or -3
#
#	-3
#	1

myEngine.setKB([])
print
print "Add 'C =  A and B' and resolve:"
myEngine.addToKB([-1,-2,3])
myEngine.addToKBAndResolve([1,-3])
myEngine.addToKBAndResolve({2,-3})
print myEngine.getKB()
print

print "Add '~C' and resolve:"
myEngine.addToKBAndResolve({-3})
print myEngine.getKB()
print

print "Add 'A' and resolve:"
myEngine.addToKBAndResolve({-1})
print myEngine.getKB()
print


print "#######################################################"
print "test case #9"
print "P1->P2, P2->P3, ..., P9->P10, ~P5 Therefore ~P4,..."
print "..., ~P3, ~P2, ~P1 "
print

# Clear KB
myEngine.setKB([])

print
print "#Start time"
print "Add P1->P2, P2->P3, ..., P99->P100, but don't Resolve"
startTime = time.time()
for i in range(1,10):
	myEngine.addToKB({-i,i+1})

elapsedTime = time.time() - startTime
print myEngine.getKB()
print "#Elapsed time: ",elapsedTime
print 

print
print "#Start time"
print "Add -P5"
startTime = time.time()
myEngine.addToKBAndResolve({-5})
elapsedTime = time.time() - startTime
print myEngine.getKB()
print "#Elapsed time: ",elapsedTime
print


print "#######################################################"
print "test case #10"
print "A->B, A->C, (B&C)->D, ~D, C Therefore ..."
print
#
#	1 -> 2
#	1 -> 3
#	2 & 3 -> 4
#
#	-4
#
#	-3
#

print "A->B, A->C, (B&C)->D"
myEngine.setKB([])
myEngine.addToKB({-1,2})
myEngine.addToKB({-1,3})
myEngine.addToKB({-2,-3,4})
print myEngine.getKB()
print

print "A->B, A->C, (B&C)->D, ~D"
myEngine.addToKBAndResolve({-4})
print myEngine.getKB()
print

print "A->B, A->C, (B&C)->D, ~D, C"
myEngine.addToKBAndResolve({3})
print myEngine.getKB()
print
