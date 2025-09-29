from pymongo import MongoClient
import os
from dotenv import load_dotenv
import barcode
from barcode.writer import ImageWriter
load_dotenv()
client= MongoClient(os.getenv("DATABASE"))
db=client['employee']
collection=db['inventory']
main_list=[0]
size_list=["S","M","L","XL","XXL"]
Sleeve_list=["FS","HS"]
Neck_list=["RN","VN","PO"]
Pattern_list=["SOL","STR","CHK","TIE"]      
print("The format for SKU id for tshirts is as follows: ")
print(f"Type(Material)-Size-Sleeve-Neck-Color-Pattern-Extra Features\n")
print(f"Intstuctions: \n")
dict1={"Size":"S,M,L,XL,XXL","Sleeve":"Full Sleeve(FS) or Half Sleeve(HS)","Neck":"Rounded Neck(RN),VN (V-neck), PO (polo)","Color":"First or first 2 letters of colours","Pattern":"SOL (solid), STR (striped), CHK (checkered), TIE (tie-dye)","Extra Features":"PK (pocket), HD (hood), MO (moisture-wicking"}
for j in dict1:
    print(f"{j}:{dict1[j]}\n")
n=int(input(f"How many iteams do u want to list?:"))
for i in range(1,n+1):
    print("\n")
    Type=input("enter type: ")
    Material=input("Enter Material: ")
    Mat=Material.removesuffix(Material[2:len(Material)])
    Type+=Mat
    while True:
        size=input("Enter size: ")
        if size in size_list:
            break
        else:
            print("Enter Valid Size")
    while True:
        Sleeve=input("Enter Sleeve: ")
        if Sleeve in Sleeve_list:
            break
        else:
            print("Enter Valid Sleeve")
    while True:
        Neck=input("Enter Neck: ")
        if Neck in Neck_list:
            break
        else:
            print("Enter Valid Neck")
    Color=input("Enter color: ")
    while True:
        Pattern=input("Enter Pattern")
        if Pattern in Pattern_list:
            break
        else:
            print("Enter Valid Pattern")
    Extra=input("Enter Extra Features")

    db.inventory.insert_many(
    [
        {
            "item":Type,
            "Material":Mat,
            "size":size,
            "Sleeve":Sleeve,
            "Neck":Neck,
            "Color":Color,
            "Pattern":Pattern,
            "Extra Features":Extra,
            "sku": f"{Type}-{size}-{Sleeve}-{Neck}-{Color}-{Pattern}-{Extra}"

        }
    ]
)
    
    sku_id=f"{Type}-{size}-{Sleeve}-{Neck}-{Color}-{Pattern}-{Extra}"
    main_list.pop()
    main_list.append(sku_id)
    print(f"sku id is: {main_list[0]}")
    data = sku_id

    barcode_class = barcode.get_barcode_class('code128')

    code128 = barcode_class(data, writer=ImageWriter())

    filename = code128.save(f"{i}_tshirt_barcode_gen")

    print(f"Barcode saved as {filename}")




