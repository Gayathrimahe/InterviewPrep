def reverse(num):
   #assign variable to hold numbers in reverse order after each execution
   rev = 0
   #declare loop to loop through each digits in a num
   while(num>0):
      #assign a variable to hold each last digit in which modulo sign gives you reminder
      # or last digit in thi case
      digit=num%10
      #now to loop through left out digits or to reverse remaining numbers assign the formula to rev
      rev=(rev*10)+digit
      num=num//10
   return rev


print(reverse(87556678))