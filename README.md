# SSW-567-HW02a

Report for Testing Classify Triangle Program

Assignment Description: 

In this assignment, we were asked to test a code that was already given, we had to create test cases apart from the ones that were already given. 
We had to report the bugs that were present in the initial test code and also fix the code with for logic to get a running working code
Author Name:  Nicole Annika Gonsalves

Summary:
Test Set 1: (Against the initial buggy implementation of classifyTriangle)
Test ID	Input	Expected Results	Actual Results	Pass or Fail
				
1001	
(classifyTriangle(3, 4, 5)
	Right	InvalidInput	Fail
1002	
(classifyTriangle(5, 3, 4)
	Right	InvalidInput	Fail
1003	
(classifyTriangle(1, 1, 1)
	Equilateral	InvalidInput	Fail
1004	
(classifyTriangle(5, 5, 8 )
	Isosceles	InvalidInput	Fail
1005	
(classifyTriangle(4, 7, 5)
	Scalene	InvalidInput	Fail
1006	
(classifyTriangle(3, 3, 15)
	NotATriangle	InvalidInput	Fail
1007	
(classifyTriangle(‘x’, ‘y’, ‘z’)
	InvalidInput	InvalidInput	Pass


Test Set 2: (Against the fixed implementation of classifyTriangle)
Test ID	Input	Expected Results	Actual Results	Pass or Fail
				
2001	
(classifyTriangle(3, 4, 5)
	Right	Right	Pass
2002	
(classifyTriangle(5, 3, 4)
	Right	Right	Pass
2003	
(classifyTriangle(1, 1, 1)
	Equilateral	Equilateral	Pass
2004	
(classifyTriangle(5, 5, 8 )
	Isosceles	Isosceles	Pass
2005	
(classifyTriangle(4, 7, 5)
	Scalene	Scalene	Pass
2006	
(classifyTriangle(3, 3, 15)
	NotATriangle	NotATriangle	Pass
2007	
(classifyTriangle(‘x’, ‘y’, ‘z’)
	InvalidInput	InvalidInput	Pass

Summary: 
Testing strategy:  
I decided to write a test for every type of Output that we were going to run. For the first test run we saw a lot of the test cases failing, because some of the logic was not implemented correctly.
After fixing the logic, I was able to pass most of the test cases.
	
Test Plan 1
	
Test Plan 2
Test Planned	7 	7
Test Executed	7	7
Test Passed	1	7
Defects Found	5	0
Defects Fixed	5	N/A


Reflection: 
I was able to understand the processes of planning your test cases and what aspects of the codes do you want to be tested. It is important to test the code multiple times using different test runs as it gives you a better perspective about the code that is currently running.
Repo Name:  SSW-567-HW02a
Repo URL:  https://github.com/nicole894/SSW-567-HW02a
Honor Pledge: I pledge my honor that I have abided by the Stevens Honor System
Detailed Results:
Assumptions -  A Right Isosceles triangle is classified as a Right triangle, even though it is a Isosceles Triangle because we are testing the Right angled property before that.
Inputs:
For Test 1001-1006 and 2001-2006 we are using integers as inputs, 
For Test 1007 & 2007, using character as input since and checking if a Type error is getting raised.
