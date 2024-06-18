import datetime
import mail
a=datetime.datetime.now()
current=a.strftime("%H:%M:%S:%p")
print(current)
f=open("bill.txt","a")
f.write(f"......SUPER MARKET......                {current}\n")
prizes=[]    
def main():
   product=["biscuit","hamam_soap","meera_shampoo","noodles","tumeric_powder","chilli_powder","pepper_powder","ponds_powder"]
   biscuit=10
   hamam_soap=51
   meera_shampoo=52
   noodles=60
   turmeric_powder=35
   chilli_powder=35
   pepper_powder=29
   ponds_powder=67
   your_order=input("enter your order ")
   if your_order in product:
      print(f"yes {your_order} is available in shop")
      try:
         how_many=int(input(f"how many {your_order} do you want"))
         if your_order=="biscuit":
            cost=biscuit*how_many
            print(f"{your_order} cost is {cost}")
            gst_percentage=float(input("enter the percentage charge for gst "))
            gst=cost*gst_percentage/100
            amount=cost+gst
            print( f"GST is {gst} and the amount is {amount}")
            prizes.append(amount)
            print(prizes)
            f=open("bill.txt","a")
            f.write(f"{your_order}    {cost}     {amount}\n")
            var=input("do you want to purchace some other things ")
            if var=="yes":
               main()
         elif your_order=="hamam_soap":
            cost=hamam_soap*how_many
            print(f"{your_order} cost is {cost}")
            gst_percentage=float(input("enter the percentage charge for gst "))
            gst=cost*gst_percentage/100
            amount=cost+gst
            print( f"GST is {gst} and the amount is {amount}")
            prizes.append(amount)
            print(prizes)
            f=open("bill.txt","a")
            f.write(f"{your_order}    {cost}     {amount}\n")
            var=input("do you want to purchase some other things ")
            if var=="yes":
               main()
         elif your_order=="meera_shampoo":
            cost=meera_shampoo*how_many
            print(f"{your_order} cost is {cost}")
            gst_percentage=float(input("enter the percentage charge for gst "))
            gst=cost*gst_percentage/100
            amount=cost+gst
            print( f"GST is {gst} and the amount is {amount}")
            prizes.append(amount)
            print(prizes)
            f=open("bill.txt","a")
            f.write(f"{your_order}    {cost}     {amount}\n")
            var=input("do you want to purchace some other things")
            if var=="yes":
               main()
         elif your_order=="noodles":
            cost=noodles*how_many
            print(f"{your_order} cost is {cost}")
            gst_percentage=float(input("enter the percentage charge for gst "))
            gst=cost*gst_percentage/100
            amount=cost+gst
            print( f"GST is {gst} and the amount is {amount}")
            prizes.append(amount)
            print(prizes)
            f=open("bill.txt","a")
            f.write(f"{your_order}    {cost}     {amount}\n")
            var=input("do you want to purchase some other things ")
            if var=="yes":
               main()
         elif your_order=="turmeric_powder":
            cost=turmeric_powder*how_many
            print(f"{your_order} cost is {cost}")
            gst_percentage=float(input("enter the percentage charge for gst "))
            gst=cost*gst_percentage/100
            amount=cost+gst
            print( f"GST is {gst} and the amount is {amount}")
            prizes.append(amount)
            print(prizes)
            f=open("bill.txt","a")
            f.write(f"{your_order}    {cost}     {amount}\n")
            var=input("do you want to purchase some other things ")
            if var=="yes":
               main()
         elif your_order=="chilli_powder":
            cost=chilli_powder*how_many
            print(f"{your_order} cost is {cost}")
            gst_percentage=float(input("enter the percentage charge for gst "))
            gst=cost*gst_percentage/100
            amount=cost+gst
            print( f"GST is {gst} and the amount is {amount}")
            prizes.append(amount)
            print(prizes)
            f=open("bill.txt","a")
            f.write(f"{your_order}    {cost}     {amount}\n")
            var=input("do you want to purchase some other things ")
            if var=="yes":
               main()
         elif your_order=="pepper_powder":
            cost=pepper_powder*how_many
            print(f"{your_order} cost is {cost}")
            gst_percentage=float(input("enter the percentage charge for gst "))
            gst=cost*gst_percentage/100
            amount=cost+gst
            print( f"GST is {gst} and the amount is {amount}")
            prizes.append(amount)
            print(prizes)
            f=open("bill.txt","a")
            f.write(f"{your_order}    {cost}     {amount}\n")
            var=input("do you want to purchase some other things ")
            if var=="yes":
               main()
         elif your_order=="ponds_powder":
            cost=ponds_powder*how_many
            print(f"{your_order} cost is {cost}")
            gst_percentage=float(input("enter the percentage charge for gst "))
            gst=cost*gst_percentage/100
            amount=cost+gst
            print( f"GST is {gst} and the amount is {amount}")
            prizes.append(amount)
            print(prizes)
            f=open("bill.txt","a")
            f.write(f"{your_order}    {cost}     {amount}\n")
            var=input("do you want to purchase some other things ")
            if var=="yes":
               main()
      except:
            print("please tell the product name coorectly")
      finally:
            def cal():
               total=sum(prizes)
               f=open("bill.txt","a")
               f.write(f"\nthe grand total is {total}\n")                
            cal()
   else:
      print("your product is not available in our super market")
main()
mail.email_sending()
            