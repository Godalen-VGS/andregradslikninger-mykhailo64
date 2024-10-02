# Finner løsninger til alle andregradslikninger på formen ax^2+bx+c=0
import math

def losninger(a, b, c):
  # Din kode her
  diskriminant = b**2-4*a*c
  if diskriminant < 0:
    return "Likningen har ingen løsning!"
  
  elif diskriminant == 0:
    return round((-b / (2*a)),2)
  
  else:
    losning1 = round(((-b + math.sqrt(diskriminant)) / (2*a)),2)
    losning2 = round(((-b - math.sqrt(diskriminant)) / (2*a)),2)
  
    return (losning1, losning2)