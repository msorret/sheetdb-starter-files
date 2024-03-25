import requests

#PASTE THE API ENDPOINT HERE
url = ""

# POST THE INFORMATION TO THE API

# DATA NEEDS TO BE CREATED AS AN OBJECT WITH KEYS THAT REFER TO THE COLUMN NAMES
data_post = {
}

requests.post(url=url, data=data_post)


# GET THE INFORMATION FROM THE API AS A JSON OBJECT
data_get = requests.get(url).json()
print(data_get)


#EXAMPLE
url = "https://sheetdb.io/api/v1/3n0u9hhrlo1bp"

# POST THE INFORMATION TO THE API

# DATA NEEDS TO BE CREATED AS AN OBJECT WITH KEYS THAT REFER TO THE COLUMN NAMES
data_post = {
}

user_name = input ("What is your name?")
user_message = input("Enter a message")
data_post = {
    'name': user_name,
    'message': user_message
}
requests.post(url=url, data=data_post)


# GET THE INFORMATION FROM THE API AS A JSON OBJECT
data_get = requests.get(url).json()
print(data_get)



