"oeis A007318"
def A007318(start: int = 0, limit: int = 20) -> Collection[int]:

    def combinaison(x, y):
      if y == x:
            return 1
      elif y == 1: 
            return x
      elif y > x:          
            return 0
      else:                
            a = math.factorial(x)
            b = math.factorial(y)
            c = math.factorial(x-y)  
            div = a // (b * c)
            return div
    
    sequence = []
    
    for i in range(start, start + limit):
        x = []
        for k in range(0,limit):
            
            if combinaison(i,k) != 0 :
                  x.append(combinaison(i,k))
        sequence.append(x)
      
    return sequence

def main():

    print(A007318(0,11))
    
if __name__=="__main__":
    main()
