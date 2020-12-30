films ={
    "K.G.F:2":[12,20],
    "Frozen":[12,5],
    "Avengers":[12,15],
    "Ala Viakunthapurramuloo":[12,30],
    "Street Dancer":[15,8],
    }

while True:

        choice=input("What film would you like to watch?:").strip().title()

        if choice in films:
                age=int(input("How old are you?:").strip())
                
                #check user age
                
                if age>= films[choice][0]:
                    #check enough seats
                        
                    num_seats = films[choice][1]
                    
                    if films[choice][1]>0:
                       print("Enjoy the film!")
                       films[choice][1]= films[choice][1]-1
                       
                    else:
                       print("We are sold out!")

                else:
                   print("Your too young to see that film!")

        else:
           print("We dont have that film...")
                        
                
