class Category:

  def __init__(self, category):
    self.category = f"{category}"
    self.ledger = []
    self.total = 0
    self.to_print = ""
    self.expenditure = 0

    # Deposit method allows to increase total of the object
  def deposit(self, amount, description = ""):
    self.ledger.append({
      "amount" : amount,
      "description" : description
    }) 
    self.total += amount

    # Function that checks if total of the object is larger than the amount to withdraw or transfer
  def check_funds(self, amount):
    if amount > self.total:
      return False
    else:
      return True
      
    # Use the check function, if True, proceeds to make the withdrawal adding the operation to the ledger
  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({      
        "amount" : -1 * amount,
        "description" : description
      })
      self.total -= amount
      self.expenditure += amount
      return True
    else:
      return False

    # Similar to withdrawal but affecting other class instance objects
  def transfer(self, amount, other_category):
    if self.check_funds(amount): 
      self.withdraw(amount, f'Transfer to {other_category.get_category()}')
      other_category.deposit(amount, f'Transfer from {self.category}')
      return True
    else: 
      return False

    # Get methods
  def get_category(self):
    return self.category
    
  def get_balance(self):
    return self.total

    # Private function to build the formatted output of the class instance
  def __build_to_print(self):
    self.to_print = '{:*^30}'.format(self.category)
    for item in range(len(self.ledger)):
      self.to_print += '\n'
      self.to_print += '{:<23}'.format(self.ledger[item]["description"][:23])
      self.to_print += '{:>7}'.format('{:.2f}'.format(self.ledger[item]["amount"])[:7])
    self.to_print += '\n'
    self.to_print += 'Total: ' + str(self.total)
    
    # Actual method to show the print version
  def __str__(self):
    self.__build_to_print()
    return self.to_print


def create_spend_chart(arg_categories):

  bar_char = "Percentage spent by category\n"
  total_expenses = 0
  percentages = []
  cat_split = []
  
  # Calculate total expenses through all cost instances
  for cat in arg_categories:
    total_expenses += cat.expenditure
    
  # Calculate cost proportion and format category name to show it in the bar chart
  for cat in arg_categories:
    cat_percent = (cat.expenditure / total_expenses) * 100 // 10
    percentages.append(cat_percent)
    cat_split += [[*cat.category]]

  # Shape first part of the bar chart showing the percentages and bar heigth
  print_percentage = 100
  for i in range(11):
    bar_char += '{:>3}'.format(print_percentage) + "|"
    for perc in percentages:
      if perc * 10 >= print_percentage:
        bar_char += ' o '
      else:
        bar_char += '   '
    print_percentage -= 10
    bar_char += ' \n'
  bar_char += 4*' '
  bar_char += 3 * len(percentages) * '-' + '-\n'

  # Shape the second part of the bar chart showing the categories names vertically
  for i in range(max([len(i) for i in cat_split])):
    bar_char += 4*' '
    for cat in cat_split:
      if len(cat) > i:
        bar_char += ' ' + cat[i] + ' '
      else:
        bar_char += 3 * ' '
    if i+1 == max([len(i) for i in cat_split]):
      bar_char += ' '
    else:
      bar_char += ' \n'

  
  return bar_char