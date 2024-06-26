# Exclusive Network Program
# Demonstrates logical operators and compound conditions

print("""
      \tExclusive Computer Network
      \t\t Members only!\n
      """)

security = 0

username = "" # Empty string

# This loop continues to ask  for a username until the user enters something
while not username:
    username = input("Username: ")

password = ""
while not password:
    password = input("Password: ")

if username == "M.Dawson" and password == "secret":
    print("Hi, Mike.")
    security = 5

elif username == "S.Meier" and password == "civilization":
    print("Hey, Sid.")
    security = 3

elif username == "S.Miyamoto" and password == "mariobros":
    print("What's up, Shigeru?")
    security = 3

elif username == "W.Wright" and password == "thesims":
    print("How goes it, Will?.")
    security = 3

elif username == "guest" or password == "guest":
    print("Welcome, guest.")
    security = 1

else:
    print("Login failed. You're not so exclusive.\n")

input("\nPress the enter key to exit.")
