#PART B - create readMe program summary covering functionality & approach

# Juli Gregson Sep. 17, 2023  CIT95 Python Mod. 3


#PART A - create program with
#create an empty list called contacts
Juli_contacts = []
Juli_contacts.append(Juli_dict)
print("\n")
print(Juli_contacts)


#create function called add_contact() takes user input to add new contact or contacts list
def add_contact(useradd_name, useradd_ph, useradd_email)
    useradd_name = input("What is your first and last name? Ex. Joe Student: ")    #User inputs name, ph & email, attempted to validate email
    useradd_ph = input("What is your area code & phone number? Ex. 000-000-0000: )  
    useradd_email = input("What is your email? Ex. joe.student@my.scccd.edu: ")                   
    Juli_dict = {"name":"useradd_name", "phone": "useradd_ph", "email:"useradd_email"}
    print(type(Juli_dict))
    return useradd_name, useradd_email, useradd_email
    print("\n\n")                                    #put name, phone, email on next line
    for key, value in Juli_dict.items():             #for loop keys and values in Juli_dict
        print(f"{key}: {value}")                     #print key & value
    print("\n\n")                        

#create function view contacts() displays list of contacts in user friendly form
def view_contacts()
    print(type(Juli_dict))
    print("\n\n")
for key, value in Juli_dict.items():
    print(f"{key}: {value}")
print("\n\n")


#create function search_contacts() takes name as input and searches for name.
        #If found, display contacts details
        #If not found, display "Contact not found"
def search_contacts()


                 

#each contact rep as dictionary - keys are name, phone, email
#Adding first contact
Juli_dict = {"name": "Juli Gregson", "phone": "559-555-1212", "email": "juli.gregson@me.com" }
print(type(Juli_dict))                           #print Juli_dict
print("\n\n")                                    #put name, phone, email on next line
for key, value in Juli_dict.items():             #for loop keys and values in Juli_dict
    print(f"{key}: {value}")                     #print key & value
print("\n\n")                                    #put each key & value on a separate line

# Adding second contact
Juli_dict = {"name": "Joe Contact1", "phone": "559-555-1213", "email": "joe.contact1@myscccd.edu" }
print(type(Juli_dict))                           #this should be a function due to repetition
print("\n\n")
for key, value in Juli_dict.items():
    print(f"{key}: {value}")
print("\n\n")

#add 3rd contact
Juli_dict = {"name": "Josephine Contact2", "phone": "559-555-1213", "email": "joesphine.contact2@myscccd.edu" }
print(type(Juli_dict))                           #this should be a function due to repetition
print("\n\n")
for key, value in Juli_dict.items():
    print(f"{key}: {value}")
print("\n\n")

# Create a list of dict objects.
# my_list_of_contacts = []
my_list_of_contacts.append(Juli_dict)
print("\n")
print(my_list_of_contacts)

# Create a third contact and append to the list
my_third_contact = {"name": "Minnie Mouse", "phone": "702-638-8388", "email": "minniem@gmail.com"}
# Output the newly created dictionary...
print("\n\n")
for key, value in my_third_contact.items():
    print(f"{key}: {value}")
print("\n\n")
# append the third contact to the list
my_list_of_contacts.append(my_third_contact)
   

#File i/o to output list of contacts to taxt file on local machine
file=open('file.txt, 'w')
    
#create user-defined methods for adding, viewing and searching
    


