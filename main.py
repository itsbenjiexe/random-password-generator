"""
Password Generator

Generates one or more random passwords based on
user-selected character types.

Name: Benji
Date: 7/22/2026
"""

import random
import string

CHAR_TYPES = {
    'uppercase': string.ascii_uppercase,
    'lowercase': string.ascii_lowercase,
    'numbers': string.digits,
    'special characters': string.punctuation
}

def get_character_pool():
    """
    Prompts the user for which character sets should be included in password generation
    """
    char_pool = {}
    for character_type in CHAR_TYPES:

        enabled = validate_string(f'Include {character_type}? (yes/no)')
        if enabled:
            
            char_pool[character_type] = enabled

    return char_pool

def generate_passwords(number_of_passwords, password_length, char_pool):
    """
    Generates a number of passwords dependent on user defined length and characters
    """
    password_list = []
    characters = ''
    if not char_pool:

        return None

    for key in char_pool:
     
        characters += CHAR_TYPES[key]

    for _ in range(number_of_passwords):

        password = ''.join(random.choice(characters) for _ in range(password_length))
        password_list.append(password)

    return password_list

def display_passwords(password_list):
    """
    Displays the generated passwords in a human-readable format
    """
    if password_list is None:

        print('Invalid Options: Restarting program now.\n')
        return
        
    for password in password_list:

        print(password)

def restart_program(password_list):
    """
    Asks the user if they would like to generate more passwords
    """
    if password_list is None :

        return True

    if not validate_string('Generate more passwords? (yes/no)'):

        return False

    return True

def validate_string(prompt):
    """
    Ensures that prompts can only be answered with yes or no (not case sensitive),
    and converts to True or False
    """
    while True:

        user_input = input(f'{prompt}: ').lower()
        if user_input not in ('yes', 'no'):

            print('Invalid Input: Please try again.')
            continue

        if user_input == 'yes':

            user_input = True

        else:

            user_input = False

        return user_input

def validate_integer(prompt):
    """
    Ensures that an integer with a value of at least 1 is entered
    """
    while True:

        try:

            user_input = int(input(f'{prompt}> '))
            if user_input < 1:

                print('Invalid Input: Please try again.')
                continue

            return user_input

        except ValueError:

            print('Invalid Input: Please try again.')

while True:

    number_of_passwords = validate_integer('Number of passwords')
    password_length = validate_integer('Length of passwords')
    char_pool = get_character_pool()
    password_list = generate_passwords(number_of_passwords, password_length, char_pool)
    display_passwords(password_list)
    if not restart_program(password_list):
        break
