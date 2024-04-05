name = input(' What\'s your name? ')

# if name == 'Harry' or name == 'Hermione' or name == 'Ron':
#   print('Gryffindor')
# elif name == 'Draco':
#   print('Slytherin')
# else: 
#   print('Who?')  

# match allows you to compare and making things more compact.
# using _ as final case is the catch all, whatever isn't handled will go to that.
  
# match name: 
#   case "Harry":
#       print("Gryffindor")
#   case "Hermione":    
#       print("Gryffindor")
#   case "Ron":
#       print("Gryffindor")
#   case "Draco"
#       print("Slytherin")
#   case _:
#       print("who? ")

# using the | allows us to basically say "or" and will allow less coding

match name: 
  case "Harry" | "Hermione" | "Ron":
      print("Gryffindor")
  case "Draco":
      print("Slytherin")
  case _:
      print("who? ")