# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 11:11:30 2023

@author: Tarnover
"""

from shodan import Shodan

# Initialize the Shodan API
api = Shodan('1eyndHbFQ004x9FbQHqZ7SbBXqLB0ECq')

while True:
    # Print the menu
    print("\n1. Search Shodan")
    print("2. Get Shodan info")
    print("3. Exit")
    
    # Prompt for a choice
    choice = input("\nEnter your choice: ")

    if choice == '1':
        # Search Shodan
        query = input("\nEnter the query: ")
        results = api.search(query)
        for result in results['matches']:
            print('IP: {}'.format(result['ip_str']))
            print(result['data'])
            print('')
    elif choice == '2':
        # Get Shodan info
        info = api.info()
        for key, value in info.items():
            print('{}: {}'.format(key, value))
    elif choice == '3':
        # Exit
        break
    else:
        print("\nInvalid choice. Please enter 1, 2, or 3.")