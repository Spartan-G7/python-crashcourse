current_users = ['madison','thomas','jack','connor','page','shiori']
new_users = ['madison','john','lillian','thomas','lauren','paul']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print('The username',user,'is already taken. Please choose a different username.')