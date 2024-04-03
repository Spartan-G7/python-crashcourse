user_names = ['john','jack','bob','admin','connor']

if user_names:
    pass
else:
    print('We need to find some users!')

for username in user_names:
    if username == 'admin':
        print('Hello',username,',would you like to see a status report?')
    else:
        print('Hello',username,', thank you for logging in again.')
