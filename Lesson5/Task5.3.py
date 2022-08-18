import random
sample_string=list(input("Enter some str..."))
for x in range(0,5):
    mix_string=random.shuffle(sample_string)
    print(mix_string)
#sample_string=list(input("Enter some str..."))
print (str(sample_string))
#a=""
#for i in sample_string:
#    a+=str(random.choice(sample_string))
#   print(a)
