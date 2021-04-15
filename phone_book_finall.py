print('welcome to phone book')



print('''

1:insert
2:search(by phone)
3:search (by number)
4:exit

''')


phone_book={}

running=False
while not running:
    select_item=input('select one item')
    if select_item.isdigit():
        select_item=int(select_item)
    
    else:
        print('welcome')

        print('''

        1:insert
        2:search(by phone)
        3:search (by number)
        4:exit

        ''')


    if select_item==1:
        name=input('enter your name :')
        phone_book[name]=[]
        item_dict={}

        contact_name=input('enter your contact name:')
        phone=input('enter your phone:')
        email=input('enter your imail:')
        addres=input('enter your addres')

        item_dict[contact_name]={
            'phone_mob':phone,
            'imail':email,
            'add':addres
        }

        phone_book[name].append(item_dict)
        print(phone_book[name])
        print(phone_book)

    

        add=True

        while add:
            continue_insert=input('add new contact (yes/no)')
            if continue_insert=='yes':
                item_dict={}
                contact_name=input('enter your contact name :')
                phone=input('enter your phone :')
                email=input('enter your imail :')
                addres=input('enter your addres:')

                item_dict[contact_name]={
                    'phone_mob':phone,
                    'imail':email,
                    'add':addres
                }

                phone_book[name].append(item_dict)
                print(phone_book[name])
                print(phone_book)

            else:
                add=False

    elif select_item==2:
        full_name=input('enter your name')
        print('contact_name'.center(15) , '|' , 'phone'.center(15)  , '|', 'imail'.center(15) , '|' , 'addres'.center(40))
        print('='*90)
        if full_name in phone_book:
            for item in phone_book[full_name]:
                for c in item:
                    print(c.center(15) , item[c]['phone_mob'].center(15) , item[c]['imail'].center(15) , item[c]['add'].center(40))

    elif select_item==3:
        phone_number=input('inter your phone num : ')
        for item in phone_book:
            for c in phone_book[item]:
                for i in c:
                    if phone_number==c[i]['phone_mob']:
                        print(item)
                    else:
                        print('not found')

    
    elif select_item==4:
        exit()
        




























            






                
        



























        





