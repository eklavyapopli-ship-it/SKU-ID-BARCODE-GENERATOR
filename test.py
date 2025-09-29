from pymongo import MongoClient
import os
from dotenv import load_dotenv
import barcode
from barcode.writer import ImageWriter
load_dotenv()
client=MongoClient(os.getenv('DATABASE'))
db=client['employee']
collection=db['inventory']


num=int(input("how many products do you have?: "))
list1=[]
list2=[]
list3=[]
for i in range(1,num+1):

    print(f"Give details for Product {i}")
    name=input("Enter name of product: ")
    if len(name)>=3:

        NamePre=name[0:3]
    else:
        NamePre=name
    list1.append(NamePre)
    n=int(input("How many categories?: "))
    for k in range(1,n+1):
        CatType=input(f"enter category {k} type: ")
        category=input(f"Enter Category{k} ")
        CatPre=category.removesuffix(category[3:len(category)])
        list1.append(CatPre)
        list2.append(category)
        list3.append(CatType)
        seperator="-"
        SKU_id=seperator.join(list1)
        format=seperator.join(list3)
    db.inventory.insert_many(
        [{
            "name":name,
             "category":list2,
             }
        ]
    )
    list1.clear()
    list2.clear()
    list3.clear()
    print(f"the format of SKU is ProductName-{format}")
    print(f"the sku id is {SKU_id}")
    data = SKU_id

    barcode_class = barcode.get_barcode_class('code128')

    code128 = barcode_class(data, writer=ImageWriter())

    filename = code128.save(f"{i}_{name}_barcode_gen")

    print(f"Barcode saved as {filename}")

    
    


    
    
