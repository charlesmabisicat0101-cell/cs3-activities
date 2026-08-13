# SG2 - Activity 1: Computational Thinking Exercise
#13 RIVERA, Chester Gabriel #14 SICAT, Charles Mabi #15 SULIGUIN, Jose Santiago | 9-Balingkilat 
## Scenario: PSHS School Canteen
### Step 1 : Identifying The Big Problem
Main Problem: The small size of the PSHS canteen causes frequent crowding and delays during student's lunch breaks. These are mainly caused due to:
- Students not being able to decide on their order, often causing more delay time
- Having to do manual calculations of the total price of items and change
- No inventory tracking
### Step 2: Identifying Three to Four Sub-Problems
#### 1. Slow Ordering
- Students in the front of the line takes too much time to decide on what to order.
#### 2. Manual Calculations
- Cashiers have to calculate the total item price and their respective changes manually, which takes some additional time.
#### 3. No Proper Inventory Tracking
- There is no system that tracks the stock of items.
#### 4. Massive Queues
- The line where students go through lacks a pre-ordering mechanism to speed up the process, making the line even longer.
### Step 3: Applying Computational Thinking Skills
| **Sub-Problem** | **CT Skill** | **Example Solution** |
| :--- | :--- | :--- |
| 1. Slow Ordering | Abstraction | Create a digital menu that clearly displays the names, pictures, and the prices. |
| 2. Manual Calculations | Algorithm Design | Develop software that accepts item quantities, automatically computes the total cost, and calculates exact change. |
| 3. No Proper Inventory Tracking  | Algorithm Design | Develop another software that works with SP#2. It tracks the stock of each item and changes every time items were computed in SP#2  . |
| 4. Massive Queues | Decomposition | Break the ordering process into distinct phases: pre-ordering, paying, and when to pick up the food. |
### Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem
#### Identified Sub-problem: SP#2: Manual Calculations
1. START PROGRAM
2. Set variables for the price of each item
3. Input the item to buy
4. Input amount of items to buy
5. Return to step 3 and 4 if customer wants more items
6. Input the cash of the customer
7. Multiply the amount of items to buy, to the price of said item. Do this for all different items bought and add them
8. Find the difference of the cash of the customer (step 6) and the price (step 7) to get the change
9. Display the process
10. END PROGRAM
