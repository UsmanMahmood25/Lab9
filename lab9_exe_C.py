"""
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
Name: lab9_exe_C.py
Assignment: Lab 9 , Exercise C
Author(s): Usman Mahmood , Deven Powell
Submission: Mar 20 , 2024
Description: Fetch data by Python.
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""

import requests
import json

def fetch_product_data(url) :
    try :
        response = requests.get(url)
        # Raises an error for bad responses
        response.raise_for_status()
        # The JSON structure includes a ' products ' key
        return response.json()['products']
    except requests.exceptions.RequestException as e :
        print (f"Error fetching data: {e}")
        return None

def list_all_products(products):
    # The for-loop will iterate through the list of the products. An if statmente is placed as error-handling, to make
    # sure the all products are accounted for. The print statement simply prints out the products, based on the 'title'
    # key. 
    for product in products:
        if 'title' in product:
            print(product['title'])
    
def search_product(products, name):
    for product in products :
        
        # The 'if-statment' handles the condition if what the user searched for was valid or invalid.
        # If choice is invalid, the for-loop will execute, and in the end print "Product not found".
        # If choice is valid, all details regarding the product will be printed, being formated to display
        # properly.
        if product['title'] == name:
            print(f"Product details for '{name}':")
            for key, value in product.items():
                print(json.dumps(product, indent=4)) #Take the specifc parameter of the string and simply formats it.
                break #break to make sure the loop does not unnecessarily loop. 
            return
    print(" Product not found.")
    
def main () :
    products_url = 'https://dummyjson.com/products'
    products = fetch_product_data(products_url)

    if products :
        while True :
            choice = input ("Choose an option:\n1. List all products\n2. Search for a product\n3. Exit\n>")

            if choice == '1':
                # runs the "Listing all prodcts"s
                list_all_products(products)
                pass
            elif choice == '2':
                # takes the argument and runs the "Search for a product"
                product_name = input (" Enter the product name : ")
                search_product(products, product_name)
            elif choice == '3':
                break
            else :
                print ("Invalid choice. Please try again.")
    else :
        print("Failed to fetch product data.")
        
if __name__ == "__main__":
    main ()