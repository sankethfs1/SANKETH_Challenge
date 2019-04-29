
def is_valid(card_number):

  #If a Card Number has only numbers then it should be 16 digit long
  #If it has '-' as well then it should be 19 digits long
  if len(card_number) not in [16, 19]:
    return False

  #If a Card Number has '-' in it then it should be in an interval of 4 digits
  if '-' in card_number:
    if card_number[4] != '-' or card_number[9] != '-' or card_number[14] != '-':
      return False

  #First digit of a Card Number should be 4, 5, or 6
  if card_number[0] not in ['4', '5', '6']:
    return False

  #Converting a string into an int
  #If there are any non-digit elements(except '-') then it should give an error
  try:
    card_number = int(''.join(i for i in card_number if i != '-'))
  except:
    return False

  #Checking if 4 consecutive digits are similar
  '''
    Basically adding 3 items in a list
    Then checking with the fourth item that if it is similar to other items in the new list or not
    If it is not then we remove the first item from the list and add the last item
  '''
  stack = []
  for i in str(card_number):
    if len(stack) == 3:
      if stack.count(i) == 3:
        return False
      stack.pop(0)
    stack.append(i)
  return True


if __name__ == '__main__':
  #Number of Card Numbers
  N = int(input())

  #Looping through inputs and checking their validity
  for _ in range(N):
    if is_valid(input()):
      print('Valid')
    else:
      print('Invalid')
