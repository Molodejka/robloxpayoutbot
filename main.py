import requests

groupIds = []
cookie = open('cookie.txt','r').readline().strip()

print('Group Payouts')

req = requests.Session()
req.cookies['.ROBLOSECURITY'] = cookie
try:
   r = req.get('http://www.roblox.com/mobileapi/userinfo').json()
   userId = int(r['UserID'])
   userName = r['UserName']
   r = req.post('https://www.roblox.com/api/item.ashx?')
   req.headers['X-CSRF-TOKEN'] = r.headers['X-CSRF-TOKEN']
except:
   input('Invalid Cookie! Can''t run checker.\nPress enter to exit...')
   exit()

percent = int(input('What percent of funds do you want to give? '))
if (percent > 100) or (percent < 1):
   input('Invalid percentage. Please enter a number between 1 and 100')
   exit()

input(f"Press enter to confirm giving {percent}% of {userName}'s groups' funds to {userName}")

data={
 "PayoutType": "Percentage",
 "Recipients": [
   {
     "recipientId": userId,
     "recipientType": "User",
     "amount": percent
   }
 ]
}

r = requests.get(f'https://groups.roblox.com/v1/users/{userId}/groups/roles').json()
for item in r['data']:
   groupIds.append(item['group']['id'])

for groupId in groupIds:
   try:
       r = req.post(f'https://groups.roblox.com/v1/groups/{groupId}/payouts',json=data)
       print(groupId,r.json())
   except Exception as e:
       print('UNKNOWN ERROR',e)

input('FINISHED')
