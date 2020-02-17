mmr=90
bronze = 50
silver = 60
gold = 70
platinum = 80

# if ( mmr > platinum):
#     print("platinum!")
# elif (mmr > gold):
#     print("gold")
# elif(mmr > silver):
#     print("silver!")
# elif(mmr > bronze) :
#     print("bronze")
# else :
#     print("Iron!")

if ( mmr > bronze):
    print("bronze!")
elif(mmr > silver):
    print("silver!")
elif (mmr > gold):
    print("gold")
elif(mmr > platinum) :
    print("platinum")
else :
    print("Iron!")


print("Your match is ready.")
