def contactList(contactInfo):
    data = contactInfo.split(' ')
    contact_name = data[0]+ ' ' + data[1]
    phone_number = data[2]
    email = data[3]
    
    return (contact_name, email, phone_number)
