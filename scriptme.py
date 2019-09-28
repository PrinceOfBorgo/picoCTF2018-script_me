# coding=utf-8

import string, sys

s = sys.argv[1] # input string to parse. The string is made of operands (balanced sequences of round brackets,
				# eventually concatenated) separeted by "+" operators, e.g. "(()(()))() + ()()(())"

stack = [] # stack used to store brackets during parsing

op = [["",0]] # list of couples [<operand>, <depth>]: <operand> is a string, <depth> is the maximum depth of the brackets
opnum = 0 # index of the current operand in the list (every time a "+" is found, add a new operand and increase opnum by 1)

opstart = 0 # index of the first character of current operand in the input string s
depth = 0 # partial brackets depth: at each ")" decrease depth by 1 and at each "(" increase depth by 1 and compare it with
		  # the maximum depth achieved up that moment (stored as second item of couples in op: op[opnum][1] = current maximum depth)

for i, c in enumerate(s): # iterate through string s characters considering the index
	if c =="(":
		stack.append((i,c)) # push "(" into the stack
		depth += 1 # increase the partial maximum depth
		op[opnum][1] = max(op[opnum][1], depth) # update the absolute maximum depth
	elif c == ")":
		j,p = stack.pop() # extract the last "(" pushed into the stack
		if p != "(":
			raise Exception("Expected \"(\" at location " + str(j) + ".")

		depth -= 1 # decrease the partial maximum depth
	elif c == "+":
		if len(stack) != 0: # if the stack is not empty, we found a "+" between brackets: error
			raise Exception("\"+\" cannot be contained in brackets.")
		
		op[opnum][0] = s[opstart:i] # save in op list the substring representing the current operand

		opnum +=1 # increase by 1 the index in op list
		opstart = i+1 # the next operand will start at position following "+"
		op.append(["", 0]) # add a new empty operand to op list
		depth = 0 # reset the partial maximum depth for the new operand

# once out of the loop we must check the last operand (the one following the last "+")

if len(stack) != 0: 
	raise Exception("\"+\" cannot be contained in brackets.")

op[opnum][0] = s[opstart:] # add the last operand to op list

# now we will use two operands op1, op2:
# op1 is the one on the left of a "+" operator, op2 is the one on the right

op1 = op[0][0] # left operand: initialized with the first in op list
depth1 = op[0][1] # depth of op1

for i in xrange(1,len(op)): # iterate through op items (skipping the first since it is already used by op1)
	op2 = op[i][0] # right operand
	depth2 = op[i][1] # depth of op2

	if depth1 == depth2: # if they have the same depth then join them with a concatenation
		op1 += op2
	elif depth1 < depth2:  # otherwise the one with lesser depth enters the first level of the other (left or right, according to its position)
		op1 = "(" + op1 + op2.strip()[1:]
		depth1 = depth2
	else:
		op1 = op1.strip()[:-1] + op2 + ")"

# after replacing op1 with the result of all the operations...

result = op1.replace(" ", "") # ... return the first operand op1 (the only one left) removing white spaces
print result