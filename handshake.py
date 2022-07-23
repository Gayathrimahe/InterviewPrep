
#n = int(input("Enter people count"))

#At the annual meeting of Board of Directors of Acme Inc. If everyone attending shakes hands exactly one time
#with every other attendee, how many handshakes are there?

def handshake_count():
    people = int(input("Enter the count of people:"))
    handshake = int(people * ((people-1)/2))
    print(handshake)
handshake_count()
