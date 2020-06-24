import socket

print("\n-----------------\nip finder\n-----------------".upper())
ans="y"
while ans == "y":
    url=input("\nEnter the website url : ".upper())
    try:
        print("\nIP : "+str(socket.gethostbyname(url)))
    except:
        print("\nInvalid Address")
    ans=input("\ndo you want to find another ip [y/n] ".upper())