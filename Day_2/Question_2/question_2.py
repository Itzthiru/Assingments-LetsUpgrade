'''ASSINGMENT SUBMISSON FOR DAY-2------THIRUMURUGAN B'''
'''Check whether a string is a pangram.'''


def checkpangram(str):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for i in alphabet:
      if i not in str.lower():
         return False
   return True


my_string = 'Jackdaws love my big sphinx of quartz.'



if(checkpangram(my_string) == True):
   print("Yes")
else:
   print("No")

