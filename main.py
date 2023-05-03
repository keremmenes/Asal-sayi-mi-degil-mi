#  Metot kendisine gelen sayı asal ise True döndürecek parametre verilmez ise default değer 2 alınacak

def asalmi(x=2):
    asal=True
    for i in range(2,int(x/2)+1):
        if x%i==0:
            asal=False
            break
    return asal

x=31
if asalmi(x):
    print (x,"asal sayidir")
else:
    print (x,"asal değildir")


print (asalmi())     #Parametresiz çağrılınca x=2 default değer geçerli olacak

a=66
i=1
while i<(a/2)+1:
    i+=1
    if a%i==0:
        print (a,"asal bir sayi degildir")
        break

else:
    print (a,"asal bir sayidir")
