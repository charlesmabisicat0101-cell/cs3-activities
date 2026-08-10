# SG2 Activity 1: Computational Thinking Exercise

* **Student Name:** Charles Mabi P. Sicat
* **Section:** 9 Balingkilat

## Scenario Analysis: PSHS School Canteen

### Step 1: Identify the Big Problem
* *Main Problem:* The PSHS school canteen is small and frequently gets crowded during lunch breaks because ordering is slow due to students taking too long to decide, manual calculations and change giving by cashiers, and a lack of real-time inventory tracking for running-out items.

---

### Step 2: Identify Three to Four Sub-Problems
1. *Ordering Inefficiency:* Students take too long to decide what to order while at the front of the line.
2. *Manual Calculation Delays:* The cashier has to manually calculate transaction totals and compute customer change.
3. *Inventory Tracking Deficit:* There is no automated system to track which food items are running low or out of stock.
4. *Queue Congestion:* The physical line lacks a structured pre-ordering mechanism to streamline traffic flow.

---

### Step 3: Define Computational Thinking Approaches

| Sub-Problem | CT Skill | Example Solution |
| :--- | :--- | :--- |
| *1. Ordering Inefficiency* | *Abstraction* | Create a digital menu interface that hides complex backend data and displays only essential item descriptions and prices clearly. |
| *2. Manual Calculations* | *Algorithm Design* | Develop a software script that accepts item quantities, automatically computes the total cost, and calculates exact change. |
| *3. Inventory Tracking* | *Data Representation* | Use structured dictionaries or JSON files to store and dynamically update available food stock counts with every completed sale. |
| *4. Queue Congestion* | *Decomposition* | Break the ordering process into distinct phases: pre-ordering, digital payment processing, and counter pickup notification. |

---

### Step 4: Pseudocode for the Transaction and Inventory Sub-Problem

```text
BEGIN CanteenTransaction
    // Initialize available inventory and prices
    Set menu_items = {"Rice": 50.00, "Chicken Adobo": 75.00, "Bottled Water": 20.00}
    Set stock_counts = {"Rice": 100, "Chicken Adobo": 80, "Bottled Water": 50}

    // Input order from student
    Print "Enter item ordered:"
    Read ordered_item
    Print "Enter quantity:"
    Read quantity

    // Check stock availability
    IF stock_counts[ordered_item] >= quantity THEN
        // Calculate total cost
        Set total_cost = menu_items[ordered_item] * quantity
        Print "Total Cost: ", total_cost

        // Process payment
        Print "Enter cash given by student:"
        Read cash_given
        
        IF cash_given >= total_cost THEN
            Set change = cash_given - total_cost
            // Update inventory
            Set stock_counts[ordered_item] = stock_counts[ordered_item] - quantity
            
            Print "Transaction Successful. Your change is: ", change
            Print "Remaining stock for ", ordered_item, " is: ", stock_counts[ordered_item]
        ELSE
            Print "Error: Insufficient cash provided."
        END IF
    ELSE
        Print "Error: Item is out of stock or requested quantity exceeds available stock."
    END IF
END CanteenTransaction
