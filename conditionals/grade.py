score = int(input('Score: '))

if score >= 90 and score <= 100:
  print("Grade: A")
elif score >= 80 and score < 90:
  print("Grade: B")
elif score >= 70 and score < 80:
  print("Grade: C")
elif score >= 60 and score < 70:
  print("Grade: D")
else: 
  print("Grade: F")

# this is same thing but a bit cleaner, python allows you to remove the comparison of and. it reads this as still score is being compared properly

if 90 <= score <= 100:
  print("Grade: A")
elif 80 <= score < 90:
  print("Grade: B")
elif 70 <= score < 80:
  print("Grade: C")
elif 60 <= score < 70:
  print("Grade: D")
else: 
  print("Grade: F")  

# simplifying even more this works because once one meets then it ends and more maintainable.
  
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
else: 
  print("Grade: F")  