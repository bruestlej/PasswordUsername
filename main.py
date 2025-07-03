def main():
  valid = True

  #asks the user for their name and password
  sName = input("What's your name? ")
  sPassword = input("Enter a desired password ")

  #defines initials using 'space' in name input
  sNames = sName.split(' ')
  sInitials = sNames[0][0] + sNames[1][0]

  #Checks password length requirements
  if not (len(sPassword) >= 8 and len(sPassword) <= 12):
    print("Password must be between 8 and 12 characters.")
    valid = False

  #Makes sure password doesn't contain 'pass' regardless of case
  Pass = "pass"
  if Pass.lower() in sPassword.lower():
    print("Password can't start with Pass.")
    valid = False

  #Checks if password contains at least 1 lowercase character
  for char in sPassword:
    c = char.islower()
    if c == True:
      break
  if c != 1:
    print("Password must contain at least 1 lowercase letter.")
    valid = False

  #Checks if password contains at least 1 uppercase character
  for char in sPassword:
    c = char.isupper()
    if c == True:
      break
  if c != 1:
    print("Password must contain at least 1 uppercase letter.")
    valid = False
    
  #check password if it contains initials of the person's name
  if sInitials.lower() in sPassword.lower():
    print("Password must not contain user initials.")
    valid = False
    
  #Defined function to see if a string contains a number or special character
  def hasNumberAndSpecialCharacter(value):

    bHasNumber = False
    bHasSpecial = False
  
    for character in value:
    
      if character.isdigit():
        bHasNumber = True

      if character in ["!", "@", "#", "$", "%", "^"]:
        bHasSpecial = True
      
    return bHasNumber, bHasSpecial

  #Checks if the password contains a number or special character
  bHasNumber, bHasSpecial = hasNumberAndSpecialCharacter(sPassword)
  
  if bHasNumber == False:
    print("Password must contain at least 1 number.")
    valid = False

  if bHasSpecial == False:
    print("Password must contain at least 1 of these special characters: !@#$%")
    valid = False
    
  #Put multiple used characters into a dictionary
  def Characters(sPassword):
    lChar = {}
    for char in sPassword:
      if char.lower() in lChar:
        #ADD one to it
        lChar[char.lower()] += 1
      else:
        lChar[char.lower()] = 1
        #Set to 1
    return lChar

  #Checks for multiple characters inside dictionary for Password given
  if any(value for value in Characters(sPassword).values() if value > 1):
    print("These characters print more than once: ")
    for key, value in Characters(sPassword).items():
      if value > 1:
        print(f"{key}: {value} times")
        valid = False

  #checks if password passed all the requirements
  if valid == True:
    print("Password is valid and OK to use.")
main()