import username_key as u

while True:
    user_id = raw_input("User ID or 'q' to quit:\n")
    if user_id == 'q':
        print "Goodbye!"
        break
    try:
        user_name = u.users[user_id]
        print "{} is {}".format(user_id, user_name)

    except KeyError:
        print "User name not found!"
