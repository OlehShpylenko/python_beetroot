list_strings=['helloworld','my','x']
for i in list_strings:
    if len(i)>=2:
        print(i[0:2],end="")
        print(i[-2:])
    elif len(i)<2:
        print()

