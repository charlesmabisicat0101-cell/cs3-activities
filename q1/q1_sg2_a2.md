# SG2 Activity 2: Code Quality Assessment

NAME and CLASS #: #13 RIVERA, Chester Gabriel A. | #14 SICAT, Charles Mabi P. | #15 SULIGUIN, Jose Santiago T. 

SECTION: 9-Balingkilat

---
#### 1. Efficiency
Which algorithm is faster when the list of numbers is very large? Why?
- Pseudocode 1 is significantly faster than Pseudocode 2 when comparing large lists of numbers because unlike Pseudocode 2, which compares each number to every other number individually, Pseudocode 1 compares the first number to the second one and uses the larger number of the two to compare to the third one and so on. Pseudocode 1 also has less loops which prevents unnecessary repetition
---
#### 2. Readability
Which algorithm is easier to understand at first glance? What makes it clearer?
- The first pseudocode is easier to understand at a first glance. That is beause the first pseudocode gets straight to the point, it calculates if a number has a greater value than a max capacity within a certain set. It is also easier to understand due to its shorter length, and it also has more understandable variable names, unlike the second pseudocode which has some unclear variable names.
---
#### 3. Maintainability
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?
- Based on the strengths of the first pseudocode, it is also easier to update or add new features in this certain algorithm rather than the second one. The first algorithm is more straightforward, which means that adding new features such as min will be easier to implement due to its simplicity. Rather than than pseudocode 2, where there’s a higher chance of bugs and errors due to its more complex nature.
---
#### 4. Testability
Which algorithm is easier to test with different inputs? Why?
- Psuedocode 1 is easier to test because of its straightforward structure, adding new steps to the code would not break it easily and there is less chance of errors when updating.
---
#### 5. Security
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?
- The two algorithms should check whether the list is empty by checking if the length of the list is above 0. It should also check if the inputs has letters or not by checking the data types is float or integers.
---
#### 6. Final Answer
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer.
