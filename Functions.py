def David ():
    print("Hello worlds")
    print("Hi guys")
David()

#Parameters
def Greetings(name, message1, message2, message3):
    print(f' Hello {name} {message1} {message2} {message3}')
Greetings('Winston', 'its now gym', 'time', 'get up')

#Arguments
def Greetings(name, message1, message2, message3):
    print(f' Hello {name} {message1} {message2} {message3}')
Greetings( "its now gym", "time", "get up" name="Winston" )