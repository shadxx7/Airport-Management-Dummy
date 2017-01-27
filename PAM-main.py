import os
import pickle
import random
import datetime

def create():  #these are all the files,lists which have being used in the program

    f1=open('flight.dat','ab')
    f1.close()
    
    o1=open('lost.dat','ab')
    o1.close()

    f2=open("passenger.dat",'ab')
    f2.close()

    t1=open('found.dat','ab')
    t1.close()

    c1=open('charter.dat','ab')
    c1.close()
    
    h=open('holiday.dat','ab')
    h.close()

    
create()

# MAIN CLASSES OF THE PROGRAM>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


        
class found:
    def __init__(self):
        self.item=''
        self.color=''
        self.description=''

    def item_data(self):
        self.item=raw_input("Enter the Name of the Item you have lost : ")
        self.color=raw_input("Enter the Color of the Item : ")
        self.description=raw_input("Give a Brief Item Description : ")
        t2=raw_input("Confirm Registration of Found Item : \ny - Yes OR n - No\n")
        if t2=='y' or t2=='Y':
            found()
        else:
            print "\nFound Item Not Resgistered\n"

    def item_display(self):
        print "Item name : ",self.item
        print "Item Color : ",self.color
        print "Brief Description of Item : \n",self.description
    
class lost:
    def __init__(self):
        self.item=''
        self.color=''
        self.description=''

    def item_data(self):
        self.item=raw_input("Enter the Name of the Item you have lost : ")
        self.color=raw_input("Enter the Color of the Item : ")
        self.description=raw_input("Give a Brief Item Description : ")
        o2=raw_input("Confirm you have lost this item : \ny - Yes OR n - No\n")
        if o2=='y' or o2=='Y':
            lost()
        else:
            print "\nLost Item Not Resgistered\n"

    def item_display(self):
        print "Item name : ",self.item
        print "Item Color : ",self.color
        print "Brief Description of Item : \n",self.description

                    
class passenger:
    def __init__(self):
      self.num=''  
      self.airlines=''
      self.name=''
      self.place_of_departure=''
      self.place_of_arrival=''
      self.seat_type=''
      self.special_service=''
      self.care=''
      self.wheel=''
      self.lounge=''
      self.dutyfree=''
      self.food=''
      self.customs=''
      self.date=''
      self.foods=''
      self.kor=0
      self.amount=0

    def store_data(self):
      self.num=raw_input("Enter your Passport No. : ")  
      self.name=raw_input("Enter your Name : ")  
      self.place_of_departure=raw_input("Enter the Place of Departure : ")
      self.place_of_arrival=raw_input("Enter the Place of Arrival : ")
      self.date=raw_input("Enter the Date of Departure (dd/mm/yy) : ")
      self.seat_type=raw_input("\nE - Economy \nB - Business \nF - First Class \nEnter your seat type : ")
      self.airlines=raw_input("\nEnter your Prefered Airlines : ") 
      self.special_service=raw_input("Do you want to take Special Services? \n\n1 - Yes \n2 - No \n")
      if self.special_service=='1':
         self.care=raw_input("Do you want any Medical Care During the flight\nY - Yes  \nN - No \n")
         if self.care=='y' or self.care=='Y':
              self.care=raw_input("Define Your Problem : ")
         else:
              self.care='None'  
         self.wheel=raw_input("Do you want a Wheel Chair Service from the Airport? \nY - Yes \nN - No \n")
         if self.wheel=='y' or self.wheel=='Y':
              self.wheel='Yes'
         else:
              self.wheel='None'
         self.lounge=raw_input("Do you want to book any Special Lounge?\nY - Yes\nN - No\n")
         if self.lounge=='y' or self.lounge=='Y':
              print "\nSelect from the following Lounge's(Please type in the entire Name) : \nVIP Lounge\nPremium Lounge\nBasic Lounge\n"
              self.lounge=raw_input()
         else:
              self.lounge='None'
      elif self.special_service=='2':
           self.special_service=='None'     
      self.food=raw_input("Do you want specific food? \n\n1 - Yes \n2 - No \n")
      if self.food=='1':
            r=['Thali','Paneer Pizza','Aloo Patties','Aloo Samosa','Fish Delights','Chicken Delights','Chicken Sandwich','Chicken Puff']
            self.food=raw_input("Do you want Vegetarian or Non-Vegetarian Food? \n1 - Veg \n2 - Non-Veg \n")
            if self.food=='1':
                print r[0:4] 
                self.foods=raw_input("\nEnter your menu (PLEASE TYPE IN THE ENTIRE NAME OF THE CHOSEN DISH): ")
        
            elif self.food=='2':
                print r[4:8]
                self.foods=raw_input("\nEnter your menu (PLEASE TYPE IN THE ENTIRE NAME OF THE CHOSEN DISH): ")
      else:
          self.food=='\nNo Specific Food Chosen.\n'
      self.customs=input("How many items do you have to declare as customs from the following :\nGold\nDisplay Screen\nEnter : ")
      if self.customs!=0:
          self.custom()
      price_allocate_tot_amount(self.airlines,self.seat_type)
      self.amount=tot_amount
      update_flight(self.airlines,self.seat_type)
      print "Flight Booked!!!!"

    def custom(self):
     for i in range(0,self.customs):
      g=raw_input("\nWhich item do you wan to declare to Declare in Customs : \n\n 1 - Gold\n 2 - Display Screen\n\n")
      g4=0
      g2=0
      self.kor
      if g=='1':
         g1=input("Enter the Amount of Gold you want to carry (in grams) : ")
         if (g1>50):
             g2=g1*130*5/100
             print "The Duty you have to Pay for the Gold you are Carrying is : Dirhams ",g2
             self.kor+=g2
         else:
             print "\nGratioz!!! You Do not Have to Pay Any Duty for That Amount of Gold!\n"
             break
      elif g=='2':
          g3=input("Enter the Screen Size(in inches) of the Display Screen : ")
          if(g3>24):
              g4=g3*40*5/100
              print "The Duty you have to Pay for the Display Screen you are Carrying is : Dirhams ",g4
              self.kor+=g4
          else:
              print "\nGratioz!!! You Do not Have to Pay Any Duty for That size of screen!\n"
              break

    def passenger_display(self):
        print "Airlines: \t Name: \t Place of Dept: \t Place of Arrival: \t Seat type: \t Special Services: \t Passport No:  \t fare amount"
        print self.airlines,'\t\t',self.name,'\t',self.place_of_departure,'\t\t\t',self.place_of_arrival,'\t\t\t',self.seat_type,'\t\t',self.special_service,'\t\t',self.num,'\t\t',self.amount
        print "\nDuty Fee To Be Paid : ",self.kor," Dirhams"
        if self.special_service=='1':
            print "\nSpecial Services : \n"
            print "Medical Care : ",self.care
            print "Wheel Chair Service : ",self.wheel
            print "Special Lounge : ",self.lounge
        else:
            print "No Special Services Selected.\n"
        if self.food=='1':
            print "\nChosen Food Dish is : \n",self.foods
        else:
            print self.food
            
        

class holiday_deals:
    
    def __init__(self):
        self.name=''
        self.num=''
        self.place_of_departure=''
        self.place_of_arrival=''
        self.seat_type=''
        self.airlines1=''
        self.hotel=''
        self.stay=''
        self.deal=''

    def store_adata(self):
      d=['Emirates','Air Arabia','Etihad']
      d1=['Economy','Business','First Class']
      d2=['Hilton Hotels','Landmark Hotels','Carlson Hotels','Starwood Hotels and Resorts','Best Western Hotels','Accor Hotels','Marriott International Resorts','InterContinental Hotel']
      self.place_of_departure=raw_input("Enter the Place of Departure : ")
      self.place_of_arrival=raw_input("Enter the Holiday Destination : ")
      self.seat_type=d1[random.randint(0,2)]
      self.airlines1=d[random.randint(0,2)]
      self.hotel=d2[random.randint(0,7)]
      self.stay=random.randint(3,7)
      self.deal=random.randint(1000,7000)
      print "For The Chosen Destination the Promotion is the following : \n","Airlines : ",self.airlines1
      print self.stay,"night stay available on this Deal with a room in ",self.hotel
      print "The Price is : ",self.deal," Dirhams per person."
      ch=raw_input("Do you wish to avail this offer? \ny - Yes or n - No\n")
      if ch=='y' or ch=='Y':
          self.name=raw_input("Enter Your Name : ")
          self.num=raw_input("Enter Your Passport No. : ")
          print "Your Booking has been confirmed!"
      elif ch=='n'or ch=='N':
          main_menu()
      else:
          print "Wrong Input \nPlease Enter the correct choice : "
          ch=input()
        
    def hol_display(self):
      print "Promotion is the following : \n","Airlines : ",self.airlines1
      print self.stay,"night stay available on this Deal with a room in ",self.hotel
      print "The Price is : ",self.deal," Dirhams per person."
      print "Name of Person Who booked the deal : ",self.name
      print "Passport No. of the Person Who booked the deal : ",self.num
      

class flight:
    def __init__(self):
        self.airline=""
        self.flight_num=""
        self.origin_name=""
        self.dest_name=""
        self.days=""
        self.time_depart=""
        self.time_arrive=""
        self.firstclass=0
        self.fir_price=0
        self.businessclass=0
        self.bus_price=0
        self.economyclass=0
        self.eco_price=0
        self.total=0
    def store_data(self):
        self.airline=raw_input("Enter the Name of the Airline : ")
        self.flight_num=raw_input("Enter the Flight Number : ")
        self.origin_name= raw_input("Enter the Place of Departure : ")
        self.dest_name=raw_input("Enter the Place of Arrival : ")
        self.days=raw_input("Enter the Date (dd/mm/yy) : ")
        self.time_depart=raw_input("Enter the Time of Departure : ")
        self.time_arrive= raw_input("Enter the Time of Arrival : ")
        self.firstclass=input("Enter the no. of First class seats : ")
        self.fir_price=input("Enter the Fare for 1 First class seat : ")
        self.businessclass=input("Enter the no. of Business class seats : ")
        self.bus_price=input("Enter the Fare for 1 Business class seat : ")
        self.economyclass=input("Enter the no. of Economy class seats : ")
        self.eco_price=input("Enter the Fare for 1 Economy class seat : ")
        self.total=self.firstclass+self.businessclass+self.economyclass
    def flight_display(self):
        print "Flight No. : ",self.flight_num
        print "Airlines : ",self.airline
        print "Place of Departure : ",self.origin_name
        print "Place of Arrival : ",self.dest_name
        print "Time of Departure : ",self.time_depart
        print "Time of Arrival : ",self.time_arrive
        print "Date of Departure : ",self.days
        print "Total no. of Business Class Seats are ",self.businessclass," at ",self.bus_price, "each."
        print "Total no. of First Class Seats are ",self.firstclass," at ",self.fir_price, "each."
        print "Total no. of Economy Class Seats are ",self.economyclass," at ",self.eco_price, "each."
        print "Total no. of Seats on the Flight are : ",self.total

class charter:
    def __init__(self):
        self.name=""
        self.time=""
        self.timeD=""
        self.timeA=""
        self.price=""

    def charter_data(self):
        self.name=raw_input("Enter Your Name : ")
        self.time=input("Enter the Total time (in hours) your Plane will be Stationed at the Airport(From time of Arrival to time of Departure) : ")
        self.timeA=raw_input("Enter the Time of Arrival: ")
        self.timeD=raw_input("Enter the Time of Departure: ")
        self.price=self.time*3000

    def charter_display(self):
        print "Name : ",self.name
        print "Total time : ",self.time
        print "Time of Arrival : ",self.timeA
        print "Time of Departure : ",self.timeD
        print "Total Amount Due : ",self.price," Dirhams"



# ALL USER CONTROLLED FUNCTIONS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def user_main_menu():
    print "\t----- Passenger Functions ----------"
    print '\t----- 0 - Search Flight ------------'
    print '\t----- 1 - Book Flight --------------'
    print '\t----- 2 - Cancel Flight ------------'
    print '\t----- 3 - Holiday Bundles ----------'
    print '\t----- 4 - Lost and Found -----------'
    print '\t----- 5 - Charter Flights ----------'
    print '\t----- 6 - Exit ---------------------'
    
    ch=input("Enter your choice : ")
    if ch==0:
        cls() 
        search_flight()
    elif ch==1:
        cls() 
        booking()
    elif ch==2:
        cls() 
        cancel_booking()
    elif ch==3:
        cls() 
        holiday_booking()
    elif ch==4:
        cls() 
        lost1()
    elif ch==5:
        cls() 
        charter1()
    elif ch==6:
        cls() 
        main_menu()
    
def holiday_booking():
    h=open("holiday.dat","ab")
    n=input("Enter The No. of Tickets you want book In this Deal: ")
    p=holiday_deals()
    for i in range(n):
        p.store_adata()
        pickle.dump(p,h)
    h.close()



def charter1():
    c1=open("charter.dat","ab")
    n=1
    c2=charter()
    for i in range(n):
        c2.charter_data()
        pickle.dump(c2,c1)
    c1.close()        

        
        
def lost1():

    print("1 - Display Found Item List\n2 - Register Lost Item\n")
    o4=raw_input("Enter You Choice : ")
    if o4=='1':
        t1=open("found.dat","rb+")
        t3=lost()
        try:
            while True:
                t3=pickle.load(t1)
                t3.item_display()
                print '\n'
        except EOFError:        
         t1.close()
         
    else:
        o1=open("lost.dat","ab")
        n=1
        o3=lost()
        for i in range(n):
            o3.item_data()
            pickle.dump(o3,o1)
        o1.close()

def booking():
    display_all_flights()
    f=open("passenger.dat","ab")
    n=input("Enter The No. of Tickets you want book : ")
    p=passenger()
    for i in range(n):
        print "ENTER DETAILS OF PASSENGER ",i+1,"\n"
        p.store_data()
        pickle.dump(p,f)
    f.close()

def cancel_booking():
    name=raw_input("Enter the Passenger Name whose Details are to be Deleted : ")
    f1=open("passenger.dat","rb")
    f2=open("newpassenger.dat","wb")
    status=0
    try:
        while True:
            p=pickle.load(f1)
            if p.name!=name:
                pickle.dump(p,f2)
            else :
                status=1
      
    except EOFError:
        f1.close()
        f2.close()
    os.remove("passenger.dat")
    os.rename("newpassenger.dat","passenger.dat")
    if status==1:
        print 'Booking canceled.'
    else:
        print 'Passenger not Found.'

        
def price_allocate_tot_amount(airline,flclass):
    f=open("flight.dat","a+b")
    status=0
    tot_amount=0
    global tot_amount
    try:
        while True:
            fl=pickle.load(f)
            if fl.airline==airline:
              if  flclass == 'F':
                tot_amount=tot_amount+fl.fir_price
                status=1
              elif flclass == 'B':
                tot_amount=tot_amount+fl.bus_price
                status=1
              elif  flclass == 'E':
                tot_amount=tot_amount+fl.eco_price
                status=1
              else:
                print "You have entered the Wrong Character for The Flight Seat Type. Please Try Again."  
                booking()
    except EOFError:
        f.close()
        if status==0:
            print "You have entered the Wrong Flight No. - Such A Flight doesn't Exist. Please Try Again."
            booking()
        print "Total Fare Amount : ",tot_amount

def update_flight(airline,flclass):
    file=open("flight.dat","rb")
    nfile=open("newflight.dat","ab")
    try:
        while True:
            fl=pickle.load(file)
            if fl.airline==airline: 
              if  flclass == 'F':
                  fl.firstclass=fl.firstclass-1
              if flclass == 'B':
                  fl.businessclass=fl.businessclass-1
              if  flclass == 'E':
                  fl.economyclass=fl.economyclass-1
              if fl.firstclass==0:
                  print "THE FIRST CLASS IS BOOKED //// PLEASE TRY FOR ANOTHER CLASS OR FLIGHT"
                  booking()
              if fl.economyclass==0:
                  print "THE ECONOMY CLASS IS BOOKED //// PLEASE TRY FOR ANOTHER CLASS OR FLIGHT"
                  booking()
              if fl.businessclass==0:
                  print "THE BUSINESS CLASS IS BOOKED //// PLEASE TRY FOR ANOTHER CLASS OR FLIGHT"
                  booking()
            pickle.dump(fl,nfile)
    except EOFError:
        file.close()
        nfile.close()
        os.remove("flight.dat")
        os.rename("newflight.dat","flight.dat")    


# ALL ADMIN CONTROLLED FUNCTIONS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class admin_login:
    def __init__(self):
        self.username=''
        self.password=''
        
    def store_data(self):
        self.username=raw_input("ENTER THE USERNAME : ")
        
        self.password=raw_input("ENTER THE PASSWORD : ")
        
        if self.username=="shubham" or self.username=="shadab" or self.username=="rohan" or self.username=="1":
            if self.password=="12345" or self.password=="1":
               print "\n----- Logged in as Administrator -----\n"
               admin_main_menu()
            else:
                x=raw_input("Do you wish to retry \nY - Yes OR n - No\n")
                if x=='y' or x=='Y':
                   al=admin_login()
                   al.store_data()
                else:
                   main_menu()
        else:
            x=raw_input("Do you wish to retry \nY - Yes OR n - No\n")
            if x=='y' or x=='Y':
                al=admin_login()
                al.store_data()
            else:
                main_menu()

def admin_main_menu():
    print "\t----- Administrator Functions ----------"
    print '\t----- 0 - Create a New Flight ----------'
    print '\t----- 1 - Delete a Flight Record -------'
    print '\t----- 2 - Modify a Flight --------------'
    print '\t----- 3 - Display Flight Details -------'
    print '\t----- 4 - Search Flight ----------------'
    print '\t----- 5 - Display Passenger List -------'
    print '\t----- 6 - Find Passenger ---------------'
    print '\t----- 7 - Holiday Deal Bookings --------'
    print '\t----- 8 - Charter Flights --------------'
    print '\t----- 9 - Lost And Found ---------------'
    print '\t----- 10 - Airplane Checkup ------------'
    print '\t----- 11 - Exit ------------------------'
    ch=input("\nEnter your choice : ")
    if ch==0:
        cls() 
        create_file()
    elif ch==1:
        cls() 
        delete()
    elif ch==2:
        cls() 
        modify()
    elif ch==5:
        cls() 
        display_details_of_passengers()
    elif ch==4:
        cls() 
        search_flight()
    elif ch==3:
        cls() 
        display_all_flights()
    elif ch==6:
        cls() 
        find_passenger()
    elif ch==7:
        cls() 
        display_holiday()
    elif ch==8:
        cls() 
        charter2()
    elif ch==9:
        cls() 
        found1()
    elif ch==10:
        cls() 
        checkup()
    elif ch==11:
        cls() 
        main_menu()
 

# all administrator functions

def display_holiday():
    c=holiday_deals()
    h=open("holiday.dat","rb")
    try:
        while True:
            c=pickle.load(h)
            c.hol_display()
            print '\n'
    except EOFError:
        h.close()
    
    

def checkup():
    h1=["Complete","In Progress","Not Started"]    
    n=random.randint(1,10)
    for i in range(1,n+1):
        print "\nFlight At Gate : ",i
        print "Fuel : ",h1[random.randint(0,2)]
        print "Security Checkup : ",h1[random.randint(0,2)]
        print "Air in Tyre's : ",h1[random.randint(0,2)]
        print "Cargo Transfer : ",h1[random.randint(0,2)],"\n"
    print    

def found1():
    print("1 - Display Found Item List\n2 - Register Found Item\n3 - Display Lost Item List\n")
    o4=raw_input("Enter You Choice : ")
    if o4=='1':
        t1=open("found.dat","rb+")
        t3=lost()
        try:
            while True:
                t3=pickle.load(t1)
                t3.item_display()
                print '\n'
        except EOFError:        
         t1.close()
         
    elif o4=='2':
        n=1
        t1=open("found.dat","ab")
        t3=found()
        for i in range(n):
             t3.item_data()
             pickle.dump(t3,t1)
        t1.close()
     
    else:
        o1=open("lost.dat","rb+")
        o3=lost()
        try:
            while True:
                o3=pickle.load(o1)
                o3.item_display()
                print '\n'
        except EOFError:        
         o1.close()
           
def charter2():
    c3=charter()
    c1=open("charter.dat","rb")
    try:
        while True:
            c3=pickle.load(c1)
            c3.charter_display()
            print '\n'
    except EOFError:
        c1.close()
    

def create_file():
    f=open("flight.dat","ab")
    n=input("Enter the no. of Flights to be added:")
    c=flight()
    for i in range(n):
        print "\nEnter the Details of Flight",i+1,"\n"
        c.store_data()
        pickle.dump(c,f)
    f.close()

def modify():
    flight_num=raw_input("Enter the Flight Name whose Details are to be Modified: ")
    f1=open("flight.dat","rb")
    f2=open("newflight.dat","wb")
    c=flight()
    status=0
    try:
        while True:
            c=pickle.load(f1)
            if c.flight_num==flight_num:
                print "Enter the details of the New Flight : "
                status=1
                c.store_data()
            pickle.dump(c,f2)
    except EOFError:
        f1.close()
        f2.close()
    os.remove("flight.dat")
    os.rename("newflight.dat","flight.dat")
    if status ==1:
        print '\nFlight Modified!\n'
    else:
        print '\nFlight not Found.\n'
        admin_main_menu()

def delete():
    id=raw_input("Enter the Flight no. whose Details are to be Deleted: ")
    f1=open("flight.dat","rb")
    f2=open("newflight.dat","wb")
    status=0
    try:
        while True:
            c=pickle.load(f1)
            if c.flight_num!=id:
                pickle.dump(c,f2)
            else :
                status=1
      
    except EOFError:
        f1.close()
        f2.close()
    os.remove("flight.dat")
    os.rename("newflight.dat","flight.dat")
    if status==1:
        print '\nFlight Deleted!\n'
    else:
        print '\nFlight not Found\n'

def display_all_flights():
    c=flight()
    f=open("flight.dat","rb")
    try:
        while True:
            c=pickle.load(f)
            c.flight_display()
            print '\n'
    except EOFError:
        f.close()

def find_passenger():
    op=raw_input("Enter the Name of the Passenger : ")
    f1=open("passenger.dat","rb")
    status=0
    p=passenger()
    try:
        while True:
            p=pickle.load(f1)
            if p.name==op:
                p.passenger_display()
                status=1
    except EOFError:
        f1.close()
    if status==0:
        print "Passenger Not Found"

def display_details_of_passengers():
    flight=raw_input("enter the name of the Flight or \nto display for all Passengers for Flights type in'all' \n")
    f1=open("passenger.dat","rb")
    status=0
    p=passenger()
    try:
        while True:
            if flight=='all':
                p=pickle.load(f1)
                p.passenger_display()
                status=1
            else:    
                p=pickle.load(f1)
                if p.airlines==flight:
                    p.passenger_display()
                    status=1
    except EOFError:
        f1.close()
    if status==0:
        print "flight not found"
        
def search_flight():
    flight_num=raw_input("Enter the Flight No. whose Details are to be Searched : ")
    f1=open("flight.dat","rb")
    status=0
    c=flight()
    try:
        while True:
            c=pickle.load(f1)
            if c.flight_num==flight_num:
                status=1
                c.flight_display()
                
    except EOFError:
        f1.close()
    if status==0:
        print '\nFlight not Found.\n'

# ALL GLOBAL FUNCTIONS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def weather():
    w2=["Sunny","Rain","Windy","Fog","Clear Sky","Dusty","Stormy Weather","Thundestorm"]
    print "TODAY'S WEATHER FORECAST IS AS FOLLOWS : \n"
    print "12:00 am to 6:00 am : ",w2[random.randint(0,7)]
    print "\n6:00 am to 12:00 pm : ",w2[random.randint(0,7)]
    print "\n12:00 pm to 6:00 pm : ",w2[random.randint(0,7)]
    print "\n6:00 pm to 12:00 am : ",w2[random.randint(0,7)]

def time():
    i = datetime.datetime.now()
    print '\nLogged in at ',
    print "\n%s/%s/%s (dd/mm/yyyy) " % (i.day, i.month, i.year)
    print "\nCurrent Time : %s:%s" % (i.hour, i.minute)

    
def cls():
    os.system('cls')
    
# MAIN MENU>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def main_menu():
    k1=open("OPEN.txt","r+")
    k2=k1.read()
    print k2
    k1.close()
    weather()
    time()
    print
    print
    b="y"
    while b=="y" or b=="Y":
        print "----------- USER LOGIN -----------"
        print "\n1.Passenger \n2.Administrator"
        print
        c=input("Enter the User Choice : ")
        print
        if c==1:
            cls() 
            user_main_menu()
        elif c==2:
            cls() 
            p=admin_login()
            p.store_data()
        else:
            print "PLEASE ENTER THE CORRECT CHOICE"
            main_menu()
        b=raw_input("Do you want to go to Main Menu :\n----- y - Yes OR n - No -----\n")
        
    else:
        exit()
main_menu()
