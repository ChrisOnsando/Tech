# A Python program to sort a list of dictionaries using Lambda

list_of_setbooks = [{"bookname"  : "CHOZI LA HERI" , "Author" : "ASSUMPTA K. MATEI" , "number of pages" : 380},
{"bookname": "KIGOGO", "Author" : "PAULINE KEA" , "number of pages" : 420},
{"bookname": "TUMBO LISILO SHIBA NA NYINGINE", "Author" : "ALIFA CHOKOCHO DUMU KAYANDA" , "number of pages" : 420},
{"bookname": "BLOSSOMS OF THE SAVANNAH", "Author" : "HENRY OLE KULET", "number of pages" : 450}]

sorted_list = sorted(list_of_setbooks, key= lambda i:i["number of pages"])

print ("The list printed by number of pages is: ", sorted_list)