from random import randint
if __name__ == "__main__":
  while True:
        wn = 1
        t1 = 0
        dn1 = True
        while dn1:
            print("What's the purchase price of a dozen?")
            purchase=input()
            if purchase.isdigit():
                purchase=int(purchase)
                break
            else:
                print("Answer must be a digit")
        dn1=True        
        while dn1:
            print("What's the selling price of a dozen?")
            sale=input()
            if sale.isdigit():
                dn1=False
                sale=int(sale)
            else:
                print("Answer must be a digit")
        dn1=True        
        while dn1:
            print("What's the salvage price of a dozen?")
            salvage=input()
            if salvage.isdigit():
                dn1=False
                salvage=int(salvage)
            else:
                print("Answer must be a digit")
        dn1=True        
        while dn1:
            print("How many weeks do you want to run?")
            weeks=input()
            if weeks.isdigit():
                dn1=False
                weeks=int(weeks)
            else:
                print("Answer must be a digit")
        dn1=True
        while dn1:
            print("How many dozen hot dogs will you order?")
            order=input()
            if order.isdigit():
                dn1=False
                order=int(order)
            else:
                print("Answer must be a digit")
        while 1<= wn <=weeks:
            die = randint(1,4)+randint(1,6)+max(randint(1,10), randint(1,10))
            if order>die:
                w1t=order*(purchase+salvage)+die*(sale-salvage)
            else:
                w1t = order*(sale+purchase)
            t1 +=w1t
            print ("On week %s, you had %s customers."  % (wn, die))
            input ("This makes this week's profit %s and your total profit %s." % (w1t, t1))
            wn+=1  
        input("Play again?")
