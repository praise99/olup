import string, random, sys

MAX_PASSWORD_LEN = 8
container = []
invalid_password_msg = 'Password is too short. At least {} chars is required'.format(MAX_PASSWORD_LEN)

def get_firstname():
    return input('Enter firstname: ')

def get_lastname():
    return input('Enter lastname: ')

def get_email():
    return input('Enter email: ')

def generate_random_password(firstname, lastname, length_of_rnd_str):
    letters = string.ascii_letters
    random_string = ''.join([random.choice(letters) for i in range(length_of_rnd_str)])
    random_pass = '{f2}{l2}{rs}'.format(f2 = firstname[:2], l2 = lastname[-2:], rs = random_string)
    return random_pass

def confirm_password(password):
    print('Your passsword is: {}'.format(password))
    res = input('Are you okay with it (Yes = Y; No = N)? ')
    if res == 'Y':
        return 1
    else:
        return 0

def choose_password():
    return input('Choose password: ')

def validate_password(password, callback):
    if len(password) >= MAX_PASSWORD_LEN:
        return password
    else:
        return callback()

def on_password_invalid():
    print(invalid_password_msg)
    password = choose_password()
    return validate_password(password, on_password_invalid)



def add_user():
    firstname = get_firstname()
    lastname = get_lastname()
    email = get_email()
    password = generate_random_password(firstname, lastname, 5)
    if confirm_password(password):
        print('\nYour password is: {}'.format(password), end='\n')
    else:
        password = validate_password(choose_password(), on_password_invalid)
    container.append({
        'firstname': firstname,
        'lastname': lastname,
        'email': email,
        'password': password
    })
    return 1

def main():
    is_success = add_user()
    if is_success:
        print('All added users are listed below...', end='\n')
        for i in range(len(container)):
            for key, value in container[i].items():
                print('{fn} = {val}'.format(fn = key.capitalize(), val = value))
            print()
    else: sys.exit(1)
    should_add_user = input('Do you want to add another user (Yes = Y; No = N)? ')
    if should_add_user == 'Y':
        main()
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()

