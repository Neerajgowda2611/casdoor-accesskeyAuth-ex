import requests

CASDOOR_URL = "https://authtest.cialabs.org/api/user"

def authenticate_user(access_key, access_secret):
    
    response = requests.get(
        CASDOOR_URL,
        params={"accessKey": access_key, "accessSecret": access_secret}
    )

    if response.status_code == 200:
        print(response.status_code)
        user_data = response.json()
        
        if "id" in user_data:
            return user_data  # Authentication successful
    return None  # Authentication failed

def process_data_request(access_key, access_secret, data):
   
    # Step 1: Authenticate the user
    user_data = authenticate_user(access_key, access_secret)

    if user_data is not None:
        # Step 2: Proceed to store the data as authentication succeeded
        # (Here you would add the code to store the data in Ciaos)
        print(data)
        print("Data stored successfully.")
        return {"message": "Data stored successfully.", "user": user_data}
    else:
        # Step 3: If authentication failed, return an error message
        return {"error": "Authentication failed. Invalid access key or secret."}

response = process_data_request(
    access_key="e89f3ac0-a424-4785-83da-9cea2b5b903d",
    access_secret="3cdfb230-d3fb-47e8-8581-7654655454a8",
    data={"some": "data"}
)

print(response)
