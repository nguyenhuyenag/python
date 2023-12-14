import json

import requests


# url = 'https://api.vdiarybook.com/api/users/profile/642a4364c93293fdbb93b802'
# http_get = res = requests.get(url, verify=False)
def get_user(user_id):
    try:
        api_url = "https://api.vdiarybook.com/api/users/profile/" + user_id
        response = requests.get(api_url, verify=False)
        # response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        user_data = response.json()
        if user_data.get('code') == 200:
            user_info = user_data.get('data', {}).get('user', {})
            # user_id = user_info.get('data_access', {}).get('user_id', '')
            # friends = user_info.get('data_access', {}).get('friends', [])
            # print(user_id)
            return user_info
            # print(f"User ID: {user_id}")
            # print("Friends:")
            # for friend_id in friends:
            #     print(f"\t- Friend ID: {friend_id}")
        else:
            print(f"Error: {user_data.get('message', 'Unknown error')}")

    except requests.exceptions.RequestException as e:
        print(f"Error making the request: {e}")


# Replace the URL with your actual API endpoint
user_id = "642a4364c93293fdbb93b802"
root_user = get_user(user_id)
friends = root_user.get('data_access', {}).get('friends', {})
data = {}
for fid in friends:
    user = get_user(fid)
    data.update(user)

# now write output to a file
twitterDataFile = open("twitterData.json", "w")
# magic happens here to make it pretty-printed
twitterDataFile.write(json.dumps(data, indent=4), indent=4, sort_keys=True)
twitterDataFile.close()
