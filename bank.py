from datetime import datetime

class Account:
  ''' has all the necessary attributes and methods to process and record any transaction associated with an instance of the bank account '''
  
  class Transaction: 
    ''' that holds the following variables for each transaction instance '''
    
    def __init__(self, transtype, amt, next = None, prev = None):
      ''' subclass Transaction that holds the following variables for each transaction instance '''
      self.trans = {transtype:amt}             # stores the transaction type and amount as a key-value pair
      self.dt = datetime.now()    # stores the datetime of the transaction
      self.next = next            # which holds the memory address of the next transaction
      self.prev = prev            # which holds the memory address of the prev transaction 
  
  
  def __init__(self, last = None, first = None, size = 0, balance = 0):
    ''' constructor method that initializes the following when an instance of a bank account is created '''
    self.last = last          # which holds the latest transaction made
    self.first = first        # which holds the earliest transaction made
    self.size = size          # which represents the number of transactions
    self.balance = balance
  
  def __len__(self):        
    ''' returns the number of transactions '''
    return self.size 

  def isEmpty(self):          
    ''' returns True is there was no recorded transaction '''
    return self.size == 0 

  @staticmethod               
  def isValidAmt(amt): 
    ''' static method isValidAmt that takes in a transaction amount '''
    try: 
      amt = float(amt)
      if type(amt)!=int and type(amt)!=float or amt<=0:
        return False
      return True
    except: 
        return False


  def deposit(self, amt):     
    ''' takes in the deposit amount as input and adds it to the balance '''
    if self.isValidAmt(amt) == False:                       # error message for invalid deposit 
      print("Invalid deposit amt: ", amt, "\n")
      return 
  
    if self.first is None:                                  # checking if inside got transaction or not, make it first and last node
      transactionNew = self.Transaction(transtype='d', amt = amt)
      self.first = transactionNew
      self.last = transactionNew
      self.first.next = None

      self.balance += amt               # add and update amount
      self.size += 1                            # update number of transactions, increment by 1
      print("First deposit: ", amt, "\n")
      return
    
    current = self.last 
    transactionNew = self.Transaction(transtype='d', amt = amt)
    current.next = transactionNew
    transactionNew.prev = current
    self.last = transactionNew                 # put the latest transaction at the last node
    
    self.balance += amt              # add and update amount
    self.size += 1                            # update number of transactions, increment by 1
    print("Deposits: ", amt, "\n")



  
  
  def withdraw(self, amt):             
    ''' takes in the the withdrawal amount as input and deducts from balance 
        should print an error message if the withdrawal amount exceeds the balance '''
     
  
    if self.isValidAmt(amt) == False:                       # error message for invalid withdrawal 
      print("Invalid withdraw amt: ", amt, "\n")
      return

    if self.balance < amt:
      print("Insufficient balance for withdrawal.", amt, "\n")
      return 

    
      
    if self.first is None: 
      transactionNew = self.Transaction(transtype='w', amt = amt)
      self.first = transactionNew
      self.last = transactionNew
      self.first.next = None

      self.balance -= amt               # add and update amount
      self.size += 1                            # update number of transactions, increment by 1
      print("Withdraw: ", amt, "\n")

      return 
    
    current = self.last 
    transactionNew = self.Transaction(transtype='w', amt = amt)
    current.next = transactionNew
    transactionNew.prev = current
    self.last = transactionNew                 # put the latest transaction at the last node
    
    self.balance -= amt                # remove and update amount
    self.size += 1                            # update number of transactions, increment by 1 
    print("Withdraw: ", amt, "\n")



    


  def getHistory(self):
    ''' prints out the account transaction history. It should display the latest transaction first. '''
    if self.first is None: 
      print("Account transaction history is empty.")  
      return 
    else: 
      n = self.last                                    # display last transaction records 
      while n is not None : 
        print(n.dt, n.trans)
        n = n.prev
      return










    

    







