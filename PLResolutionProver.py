
# PLResolutionProver.py , version 1.0.0, April 30, 2017
#
# Minimalist Propositional Logic Resolution (Theorem) Prover
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
# a)	You are permitted to use this source code for personal 
#		and/or commercial purposes.
# b)	You may redistribute this text as part of a project 
#		ONLY IF this legal agreement remains, and any 
#		changes/additions to the text or documentation are 
#		clearly marked.
# c)	This source code is provided "as is", with NO WARRANTY of 
#		any kind, express or implied, not even "fitness for 
#		a particular purpose".
# d)	Erich Glinker shall not be held liable under any 
#		circumstances for any damage resulting from the use 
#		or misuse of this source code.
# e)	In jurisdictions where any part of this legal agreement 
#		is not legal or not enforceable by law, part 'e' shall 
#		remain upheld, and you are expressly forbidden to use 
#		this text for any purpose.
#
#
# DESCRIPTION
#
# This module is a propositional logic theorem prover that is small and has 
# a minimalist API and is designed to be easy to use. The prover uses 
# propositional resolution as it's inference mechanism.
#  
# The knowledgebase (KB) is represented in conjunctive normal form (a 
# conjunction if disjunctions).  Each disjunctive clause is represented as 
# python set of positive or negative propositions (where propositions are 
# represented as positive and negative integers:
#
# Example:    The disjunctive clause (A or B or not C) is equivalently 
# represented as the following python set in the knowledgebase:    
#conjunctiveClause = {1,2,-3}    
#
# Internally the knowledge base is represented as a python list of python 
# sets (again, the python sets are the conjunctive clauses:
#
# Example:  KB  = (A or B or not C) and (C or D or E) is represented as: 
# KB = [{1,2,-3}, {3,4,5}]
#
# The prover is small, but it has few optimizations for speed. 
#
# ------------------------------------------------------------------------------
# API 
# ------------------------------------------------------------------------------
# getKB()	 - Returns the knowledge base of the PLResolutionProver object 
# as a list of lists representing the knowledgebase in conjunctive normal 
# form (inner lists each representing a disjunctive clause)
#
# Example:
# >>># KB = (A or C or E) and (not E or G or . . .
# >>>print   myPLResolutionProver.getKB()  
# [[1, 3, 5], [-5, 7, -6], [63, -23, 49], . . . . . 
#
# ------------------------------------------------------------------------------
#
# setKB(KBInput) -  Takes a list of lists as an input argument representing a 
# knowledgebase in conjunctive normal form (inner lists each representing a 
# disjunctive clause).
#
# Example:
# >>> setKB([1,2],[-2,3]) # Set the content of the knowlegebase. 
# >>> print   myPLResolutionProver.getKB()  # Print content of knowledgebase.
# [[1,2],[-2,3]]
#
# Example:
# >>>#To empty the knowlegebase type the following:
# >>>setKB([]) # Set the content of the knowlegebase to an empty list
# ------------------------------------------------------------------------------
#
# addToKBAndResolve(disjunctiveClause) -  Add a disjunctive clause to the 
# knowledgebase and apply resolution inference rule between each the new clause 
# and each relevant clause in the KB to derive new clauses.  If new clauses are 
# formed then resolve the newly formed clauses with the relevant parts  KB as 
# well.
#
# Example:
# >>> setKB([-1,2],[-2,3]) # Set the content of the knowlegebase. 
# >>> print   myPLResolutionProver.addToKBAndResolve([-3]) # Add and resolve.
# >>> print   myPLResolutionProver.getKB()  # Print content of knowledgebase.
# [[-1,2], [-2,3], [-3], [-2], [-1]]
#
# ------------------------------------------------------------------------------
#
# addToKB(disjunctiveClause) -  Add a disjunctive clause to the knowledgebase 
# and without applying resolution inference rule to each the new clause.
#
# Example:
# >>> setKB([-1,2],[-2,3]) # Set the content of the knowlegebase. 
# >>> print   myPLResolutionProver.addToKB([-3]) # Add and resolve.
# >>> print   myPLResolutionProver.getKB()  # Print content of knowledgebase.
# [[-1,2], [-2,3], [-3]]
#  
# ------------------------------------------------------------------------------ 

import numpy as np
import time
from itertools import groupby 
 
# This is a class definition for a simple propsitional logic prover.
# It is designed to be easiy to use even by those not too fammiar
# with how propositioal logic provers are implemented.
class	PLResolutionProver: 

	def __init__(self):
		# The knowlege base.  
		self.KB = []	
		
		# Dictionary that map propositons to indexes of disjunctive clauses.
		self.KBDictionary = {0:[0]}	
		
		# Empty set used to save time in methods that use empty set for
		# comparison repeatedly.
		self.emptySet = set()


	# Add a disjunctive clause to the knowledgebase 
	# and without applying resolution inference rule to each the new clause.
	def	addToKB(self, a):
		if a not in self.KB:
			self.KB.append(set(a))
			ruleIndex = len(self.KB)-1
			for i in a:
				if i not in self.KBDictionary.keys():
					self.KBDictionary[i] = []
				self.KBDictionary[i].append(ruleIndex)

	
	# This function is just her to help out addToKBAndResolve(self, a) 
	def findRuleIndexes(self, i):
		ruleIndexesOut = []
		for k in list(self.KB[i]):
			if -k in self.KBDictionary.keys():
				ruleIndexesOut.extend(self.KBDictionary[-k])
		return ruleIndexesOut
	
	
	# Add a disjunctive clause to the knowledgebase and apply resolution 
	# inference rule between each the new clause and each relevant clause 
	# in the KB to derive new clauses.  If new clauses are formed then 
	# resolve the newly formed clauses with the relevant parts  KB as 
	# well.
	def addToKBAndResolve(self, a):
		self.addToKB(a)	
		emptySet = set()
		i = len(self.KB)-1
		l = 0
		while True:
			ruleIndexes = self.findRuleIndexes(i)			
			for	j in ruleIndexes:
				l = l + 1
				#print 'j',j
				(a,b)=(self.KB[i],self.KB[j])	
				literalsOverlap = a & set(-np.array(list(b)))
				if len(literalsOverlap)==1:
					r = (a-literalsOverlap)|b-set(-np.array(list(literalsOverlap))) 			
					self.addToKB(r)
			if(i==len(self.KB)-1):
				break
			i = i + 1
		return [l, len(self.KB)-1]
		
		
	# Returns the knowledge base of the PLResolutionProver object 
	# as a list of lists representing the knowledgebase in conjunctive normal 
	# form (inner lists each representing a disjunctive clause)	
	def getKB(self):
		#print [list(x) for x in self.KB]
		return [list(x) for x in self.KB]


	# Takes a list of lists as an input argument 
	# representing a knowledgebase in conjunctive normal form (inner lists 
	# each representing a disjunctive clause).	
	def setKB(self,KBInput):
		self.KB=[]
		self.KBDictionary = {0:[0]}
		for x in KBInput:
			self.addToKB(x)



