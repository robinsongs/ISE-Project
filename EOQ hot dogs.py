
from random import randint
if __name__ == "__main__":
  while True:
    input("(press enter to proceed text)")
    input("You sell hot dogs.")
    input("As a humble small business owner, you have only one guideline,")
    input("(your hot dogma, so to say):")
    input("Make as Much Money as Possible")
    answer=True
    while answer:
        print("Make sense? y/n")
        yn = input()
        if yn == "y":
          print("slay")
          answer = False
        elif yn == "n":
          print ("one more time")
        else:
          print ("(y means yes and n means no. type the letters.)")
    print("Let's start with your name: ")
    name = input()
    input("Cool, that's never going to be used again.")
    input("Anyways")
    input("Let's lay down some ground rules:")
    print("A dozen hot dog buns cost $4, and a dozen hot dog dogs cost $5.")
    input("Meanwhile, you can sell hot dogs for $1.75 each")
    print("The number of customers per week will be determined by rolling three six-sided die.")
    print("Each customer will buy a dozen hot dogs.")
    input("(this is to keep the profits high enough without this taking five years)")
    print("You'll buy a consistent number of dog dozens per week.")
    print("Any unsold dog dozens will be thrown in the trash at the end of the week.")
    input("You'll have ten weeks this round.")
    print("Now, with all of that in mind-")
    dn1 = True
    while dn1:
        print("How many dozen hot dogs do you want to sell each week?")
        dognumber1=input()
        if dognumber1.isdigit():
            print("slay")
            dn1=False
            dognumber1=int(dognumber1)
        else:
            print("not slay. try again")
    wn = 1
    t1 = 0
    purchase = -9
    salvage = 0
    sale = 21
    weeks = 10
    while 1<= wn <=weeks:
        die = randint(1,6)+randint(1,6)+randint(1,6)
        if dognumber1>die:
            w1t=dognumber1*(purchase+salvage)+die*(sale-salvage)
        else:
            w1t = dognumber1*(sale+purchase)
        t1 +=w1t
        print ("On week %s, you had %s customers."  % (wn, die))
        input ("This makes this week's profit %s and your total profit %s." % (w1t, t1))
        wn+=1  
    input("Wow, %s dollars!" % (t1))
    input("I'll let you decide if that's good or not.")
    input("I'll let you in on a little secret, though:")
    input("There's a better way to do this.")
    print("In fact, there's a formula:")
    input("R = Cu/(Cu+Co)")
    input("-first, though, we have to define the variables.")
    print("Co is the cost of overage")
    print("This refers to the money you lose for having excess stock.")
    print("It's defined as price of purchase - price of salvage.")
    input("Here, it's the cost of buying one dog dozen, so $9.")
    print("Cu is the cost of underage")
    print("This refers to the profit you lose for having insufficient stock")
    print("It's defined as the price of sale - price of purchase.")
    input("Here, it's the profit per dozen")
    print("That's income per dozen ($21) minus cost per dozen ($9), which is $12")
    input("That puts our ratio at 12/(12+9), or about 0.57")
    input("What do we do with that, though?")
    input("Well, the ideal order quantity is the one where the probability of a customer ordering that amount or less is the smallest probability greater than our ratio.")
    input("The cumulative probability chart for a 3d6 distribution is as follows:")
    x = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    y= [.0046,.0185,.0463,.0926,.162,.2593,.375,.5,.625,.7407,.838,.9074,.9537,.9815,.9954,1]
    for index, item in enumerate(zip(x,y)):
        print (item)
    input()
    print("That makes our ideal number the one with the ratio right above 0.57,")
    input("meaning the perfect amount of dogs to order is 11!")
    input("Knowing this, we can find the ideal order number in any situation!")
    input("...and since this can be applied to any scenario, it'd be boring to just retry this one")
    input("So let's try something a little more fun:")
    print("New rules!")
    print("Hot dog buns are now $1.25 per 3 pack")
    input("Hot dog dogs are now $3 per 4 pack")
    print("Each individual hot dog is $2.75, but people still only buy them by the dozen")
    input("Additionally, you can now sell unused dogs for $2 a dozen.")
    input("And you have fifteen weeks.")
    print("Finally, our dice rules have changed.")
    print("Instead of three six-sided die, we are now calculating demand using")
    print("One four-sided dice")
    print("plus one six-sided die")
    input("plus the highest of two ten-sided dice.")
    input("...here's the cumulative probability table to that one. I'm not a monster.")
    x = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18, 19, 20]
    y= [.0004,.0025,.0083,.0208,.0433,.0792,.1312,.2017,.2917,.4017,.5229,.6458,.7600,.8542,.9250,.9692,.9921,1]
    for index, item in enumerate(zip(x,y)):
        print (item)   
    input("(you can scroll up to check this at any time)")
    input("Now.")
    dn1 = True
    while dn1:
        print("How many dozen hot dogs do you want to sell each week?")
        dognumber1=input()
        if dognumber1.isdigit():

            print("slay")
            dn1=False
            dognumber1=int(dognumber1)
        else:
            print("not slay. try again")
    wn = 1
    t1 = 0
    sale = 33
    purchase = -14
    salvage = 2
    weeks=15
    while 1<= wn <=weeks:
        die = randint(1,4)+randint(1,6)+max(randint(1,10), randint(1,10))
        if dognumber1>die:
            w1t=dognumber1*(purchase+salvage)+die*(sale-salvage)
        else:
            w1t = dognumber1*(sale+purchase)
        t1 +=w1t
        print ("On week %s, you had %s customers."  % (wn, die))
        input ("This makes this week's profit %s and your total profit %s." % (w1t, t1))
        wn+=1  
    input("You made a total of $%s, with your average weekly profit being $%s" % (t1, t1/weeks))
    input("Your ideal number would have been the one closest above .6129, which is 14.")
    print("Your estimated weekly income with 14 is around $213 (making the predicted total $3195).")
    input("Of course, though, there are many causes for variation here, so the expected total might not always be accurate.")
    input("If you're interested in running this simulation yourself, feel free to mess with the code as much as you like!")
    input("You can also always play again if you want. ")
    print("(that's it. slay.)")
    input("Thanks for playing, %s!" % (name))