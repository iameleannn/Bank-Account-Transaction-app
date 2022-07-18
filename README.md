# Bank-Account-Transaction-app



# Introduction
This project is to work on Data Structures and Algoithms with Python by getting familar with classes and linked lists. In many industries, there exists many formulas or algorithms, and the techniques learnt can be applied in other areas as well.

![account_transaction](https://i.ibb.co/qBj0ZPV/mobile-mbanking-account-transaction.png)


# Background
A bank account is a financial account that is maintained by a bank or financial institution, and is used to record the financial transactions between the bank and the customer. With the advent of smartphones, banks have introduced mobile banking, and account holders are now able to track their transaction history this has allowed them to make a more informed financial decisions in a timely manner. 


## Task

The task is to implement a simple banking account transaction program, that tracks and records each transaction done within that account. To use a doubly-linked list where each node represents a transaction. To simplify the problem, we shall only consider 2 types of transaction:

- Deposit: To represent any fund addition to the account
- Withdrawal: To represent any fund deduction from the account

In order to do this, we are to implement the class `Account` that has all the necessary attributes and methods to process and record any transaction associated with an instance of the bank account. It **MUST** include the following:

- subclass `Transaction` that holds the following variables for each transaction instance:
 - `trans` which stores the transaction type and amount as a key-value pair
 - `dt` which stores the datetime of the transaction (Hint: you may use the `datetime` module)
 - `next` which holds the memory address of the next transaction (default value of `None`)
 - `prev` which holds the memory address of the prev transaction (default value of `None`)
- constructor method that initializes the following when an instance of a bank account is created:
 - `last` which holds the latest transaction made (default value of `None`)
 - `first` which holds the earliest transaction made (default value of `None`)
 - `size` (default value of 0) which represents the number of transactions
 - `balance` (default value of 0)
- method `__len__` that returns the number of transactions.
- method `isEmpty` that returns True is there was no recorded transaction
- static method `isValidAmt` that takes in a transaction amount (withdraw or deposit) and returns True if the input is valid (accepts only positive numbers)
- method `deposit` that takes in the deposit amount as input and adds it to the balance.
- method `withdraw` that takes in the the withdrawal amount as input and deducts it from the balance. It should print an error message if the withdrawal amount exceeds the balance.
- method `getHistory` that prints out the account transaction history. It should display the latest transaction first.
- any other classes, attributes or methods that you think is necessary

We are to use **docstrings** to summarize the functionality and list down the members (subclasses, varibles, methods) within the class. Each subclasses and methods should have their own docstrings.



# Pros and cons of using a doubly linked list in such applications as compared to a singly linked list or just a list

compare pros with singly linked list/list 
- Able to reverse transverse as compared to singly linked list. 
- Ability to allocate or reallocate the memory easily when it is executing. 
- Bidirectional is possibility. 
- Easier to delete nodes as only required pointer to be deleted compared to singly linked list. 
- Time complexity of insertion is half of single linked list as only 1 node is required. 


compare cons with singly linked list/list 
- It uses additional memory as compared to singly linked list. 
- No direct access is allowed as memory is stored randomly. 



