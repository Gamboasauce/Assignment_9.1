import os.path

print(os.getcwd())

def directory():
    while True:
        user_directory = input("What is the name of the Directory? :")

        if not os.path.isdir(user_directory):
            print('Directory {user_directory} does not exist')
        else: 
            break
            
def file():
    user_file = input('Create a file name: ')
    user_name = input('What is your name?: ')
    user_address = input('What is your address?: ')
    user_digits = input('What is your phone number?: ')

    f= open (user_file,"w+")
    f.write(user_name)
    f.write(user_address)
    f.write(user_digits)
    f.close

directory()
file()

