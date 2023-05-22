

class Product :
   

    def Cart(self,quantityA,quantityB,quantityC,gwrap):

         # list1 is a dict. of quantity of products
        list1={'A':0,'B':0,'C':0}

        #list2 is a dict. of price of products
        list2={'A':20,'B':40,'C':50}

        self.quantityA=quantityA
        self.quantityB=quantityB
        self.quantityC=quantityC
        self.gwrap=gwrap
        #update dict. with required quantity  of products
        list1['A']=quantityA
        list1['B']=quantityB
        list1['C']=quantityC
        pa=list2['A']
        pb=list2['B']
        pc=list2['C']
        stotalA=quantityA*pa
        stotalB=quantityB*pb
        stotalC=quantityC*pc

       


        #print quantity and sub total amount for each item
        if list1['A']!=0:
            print(f"product = A  Quantity= {list1['A']}  total amount/item = {stotalA}$")
        if list1['B']!=0:
            print(f"product = B  Quantity= {list1['B']}  total amount/item ={stotalB}$")
        if list1['C']!=0:
            print(f"product = C  Quantity= {list1['C']}  total amount/item ={stotalC}$")  

        
        #print total amount and total quantity
        totalamount= stotalA+stotalB+stotalC
        totalquantity= quantityA+quantityB+quantityC
        print(f'total amount = {totalamount}$')
        print(f'total quantity = { totalquantity}')

        #list3 is a dict. of total amount after discounts applied
        list3={"tiered_50_discount":0,"flat_10_discount":0,"bulk_10_discount":0,"bulk_5_discount":0}

        #Checking for 50 % discount
        if totalquantity >30 :
            discount_type="tiered_50_discount"
            

            if list1['A'] >15 and list1['B'] >15 and list1['C'] >15 :

                
                discounted_totalamount= 15*list2['A']+(((list1['A']-15)*list2['A'])-(list1['A']-15)*list2['A']*(50/100))+ 15*list2['B']+(((list1['B']-15)*list2['B'])-(list1['B']-15)*list2['B']*(50/100))+15*list2['C']+(((list1['C']-15)*list2['C'])-(list1['C']-15)*list2['C']*(50/100))
                                        
                                        
                list3["tiered_50_discount"]= discounted_totalamount

            elif list1['A'] >15 and list1['B'] <=15 and list1['C'] <=15 :

                discounted_totalamount= 15*list2['A']+(((list1['A']-15)*list2['A'])-(list1['A']-15)*list2['A']*(50/100))+stotalB+stotalC
                list3["tiered_50_discount"]= discounted_totalamount   

            elif list1['A'] <=15 and list1['B'] >15 and list1['C'] <=15 :

                discounted_totalamount= 15*list2['B']+(((list1['B']-15)*list2['B'])-(list1['B']-15)*list2['B']*(50/100))+stotalA+stotalC
                list3["tiered_50_discount"]= discounted_totalamount

            elif list1['A'] <=15 and list1['B'] <=15 and list1['C'] >15 :

                discounted_totalamount= 15*list2['C']+(((list1['C']-15)*list2['C'])-(list1['C']-15)*list2['C']*(50/100))+stotalA+stotalB
                list3["tiered_50_discount"]= discounted_totalamount

            elif list1['A'] >15 and list1['B'] >15 and list1['C'] <=15 :

                discounted_totalamount= 15*list2['A']+ (((list1['A']-15)*list2['A'])-(list1['A']-15)*list2['A']*(50/100)) +15*list2['B']+(((list1['B']-15)*list2['B'])-(list1['B']-15)*list2['B']*(50/100)) +stotalC
                list3["tiered_50_discount"]= discounted_totalamount

            elif list1['A'] <=15 and list1['B'] >15 and list1['C'] >15 :

                discounted_totalamount= 15*list2['C']+(((list1['C']-15)*list2['C'])-(list1['C']-15)*list2['C']*(50/100))+15*list2['B']+(((list1['B']-15)*list2['B'])-(list1['B']-15)*list2['B']*(50/100))+stotalA
                list3["tiered_50_discount"]= discounted_totalamount

            elif list1['A'] >15 and list1['B'] <=15 and list1['C'] >15 :

                discounted_totalamount=15*list2['A']+ (((list1['A']-15)*list2['A'])-(list1['A']-15)*list2['A']*(50/100))+15*list2['C']+(((list1['C']-15)*list2['C'])-(list1['C']-15)*list2['C']*(50/100))+stotalB
                list3["tiered_50_discount"]= discounted_totalamount                           

            
            
        #checking for flat_10_discount
        if totalamount >200 :
            discount_type="flat_10_discount"
            
            discounted_totalamount= totalamount-(totalamount*(10 /100))
            list3["flat_10_discount"]= discounted_totalamount


        #checking for bulk_10_discount

        if totalquantity >20 :
            discount_type="bulk_10_discount"
            
            discounted_totalamount= totalamount-(totalamount*(10 /100))
            list3["bulk_10_discount"]= discounted_totalamount


        #checking for bulk_5_discount    

        if list1['A'] >10 and list1['B'] >10 and list1['C'] >10 :

            discounted_totalamount= (stotalA-(stotalA*(5 /100)))+(stotalB-(stotalB*(5 /100)))+(stotalC-(stotalC*(5 /100)))
            list3["bulk_5_discount"]= discounted_totalamount

        elif list1['A'] >10 and list1['B'] <=10 and list1['C'] <=10 :
            
            discounted_totalamount= (stotalA-(stotalA*(5 /100)))+stotalB+stotalC
            list3["bulk_5_discount"]= discounted_totalamount

        elif list1['A'] <=10 and list1['B'] >10 and list1['C'] <=10 :
            
            discounted_totalamount= (stotalB-(stotalB*(5 /100)))+stotalA+stotalC
            list3["bulk_5_discount"]= discounted_totalamount

        elif list1['A'] <=10 and list1['B'] <=10 and list1['C'] >10 :
            
            discounted_totalamount=(stotalC-(stotalC*(5 /100)))+stotalA+stotalC
            list3["bulk_5_discount"]= discounted_totalamount

        elif list1['A'] >10 and list1['B'] >10 and list1['C'] <=10 :
            
            discounted_totalamount= (stotalA-(stotalA*(5 /100)))+(stotalB-(stotalB*(5 /100)))+stotalC
            list3["bulk_5_discount"]= discounted_totalamount

        elif list1['A'] <=10 and list1['B'] >10 and list1['C'] >10 :
            
            discounted_totalamount= (stotalB-(stotalB*(5 /100)))+(stotalC-(stotalC*(5 /100)))+stotalA
            list3["bulk_5_discount"]= discounted_totalamount

        elif list1['A'] >10 and list1['B'] <=10 and list1['C'] >10 :
            
            discounted_totalamount= (stotalA-(stotalA*(5 /100)))+(stotalC-(stotalC*(5 /100)))+stotalB
            list3["bulk_5_discount"]= discounted_totalamount

        #discount_list is the list of doscounted total amount
        print(list3)
        discount_list=(list3.values())

        print(discount_list)
        #removing zeroes from the list
        discount_list= [i for i in discount_list if i != 0]

        #if list is empty, then no discounts are applicable
        if discount_list!=[]:
        #finding min. value from the list to find most beneficial discount for the customer
            highest_discount=min(discount_list)

            discount_applied=list(list3.keys())[list(list3.values()).index(highest_discount)]

        #applying discount for total amount

            netamount=highest_discount
            print(f'discount applied : {discount_applied}$')
            print(f'net amount after discount :{netamount}$')

        else: 
            
            netamount=totalamount
            print('no discounts applicable')

        #gif wrap is 1$ per unit
        if gwrap == 'y':
            netamount=netamount+1

            print ('gift wrap charge: 1$')
        else :
            print('gift wrap charge: 0$')

        #shipping charge is 5$ per package.each package contains 10 units max.

        if totalquantity % 10 !=0 :
            ship=(int(totalquantity/10)+1)*5
        else :
            ship=(int(totalquantity/10))*5

        #printing shipping charge and total amount
        print(f'shipping charge = {ship}$')

        print (f'total = {ship+netamount}$')





print('''
 *******Product Catelog********

 PRODUCT A   ---- 20$
 PRODUCT B   ---- 40$
 PRODUCT C   ---- 50$''')





    
# enter quantity for each product  
quantityA= int(input('Quantity required for A: '))
quantityB= int(input('Quantity required for B: '))
quantityC= int(input('Quantity required for C: '))
 #prompt for giftwrap
gwrap= (input('gift wrap required? (y/n)')).lower()
obj=Product()
obj.Cart(quantityA,quantityB,quantityC,gwrap)