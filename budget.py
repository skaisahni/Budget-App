class Category():

    def __init__(self,category):
        self.category = category
        self.ledger = []
        self.operations = [] #This an auxiliar list where we keep the balance of a current category. 
    
    def check_funds (self,amount):
        if float(amount)<=sum(self.operations):
            return True
        else:
            return False
        
    #Now, let's create the methods 
    def deposit (self,amount,description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.operations.append(float(amount))
        
    def withdraw (self,amount,description=""):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": description})
            self.operations.append(-float(amount))
            return True
        else:
            return False
        
    def get_balance (self):
        current_balance = sum(self.operations)
        return current_balance
        
    #Now, the transfer capability
    def transfer (self, amount, d):
        if self.check_funds(amount) == True:
            self.withdraw(amount, f"Transfer to {d.category}")
            d.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False
    
    #Now, let's find the  way to print out the category name and the ledge
    def __str__(self):  
        y = "{:*^30s}".format(f"{self.category}") + "\n"
        for item in self.ledger:
            y = y + f"{item['description'][:23].ljust(23)}"+ "{:.2f}".format(item['amount']).rjust(7) + "\n"
        total = self.get_balance()
        y = y + "Total: " + "{:.2f}".format(total)
        return y




def create_spend_chart(categories):
  category_names = []
  spent = []
  spent_percentages = []

  for category in categories:
    total = 0
    for item in category.ledger:
      if item['amount'] < 0:
        total = total- item['amount']
    spent.append(round(total, 2))
    category_names.append(category.category)

  for amount in spent:
    spent_percentages.append(round(amount / sum(spent), 2)*100)

  graph = "Percentage spent by category\n"

  labels = range(100, -10, -10)

  for label in labels:
    graph += str(label).rjust(3) + "| "
    for percent in spent_percentages:
      if percent >= label:
        graph += "o  "
      else:
        graph += "   "
    graph += "\n"

  graph += "    ----" + ("---" * (len(category_names) - 1))
  graph += "\n     "

  longest_name_length = 0

  for name in category_names:
    if longest_name_length < len(name):
      longest_name_length = len(name)

  for i in range(longest_name_length):
    for name in category_names:
      if len(name) > i:
        graph += name[i] + "  "
      else:
        graph += "   "
    if i < longest_name_length-1:
      graph += "\n     "

    

  return(graph)