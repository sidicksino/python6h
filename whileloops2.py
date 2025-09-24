# # 1er partie 
# # command = ''
# # while command != 'QUIT':

# # 2eme partie
# while True:
#     command = input("> ").upper()
#     if command == 'HELP':
#         print('''
# Stop - to stop car!
# Start - to start car!
# Quit to exit!
#         ''')
#     elif command == 'START':
#         print('Car Started !')
#     elif command == 'STOP':
#         print('Car stopped !')
#     elif command == 'QUIT':
#         break
#     else:
#         print("Sorry I don't understant")


# 3eme partie
car_started = False

while True:
    command = input("> ").upper()
    
    if command == 'HELP':
        print("""
Start - to start the car!
Stop - to stop the car!
Quit - to exit!
        """)
    
    elif command == 'START':
        if car_started:
            print("Car is already started!")
        else:
            car_started = True
            print("Car started!")
    
    elif command == 'STOP':
        if not car_started:
            print("Car is already stopped!")
        else:
            car_started = False
            print("Car stopped!")
    
    elif command == 'QUIT':
        break
    else:
        print("Sorry, I don't understand that command.")
