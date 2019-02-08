import requests
#/from browser : inspect / network tab / Headers = headers / Form Data = login_data
with requests.Session() as s:
    url = "https://thesiteyouloginto.com/sign-in/"
    headers = {"user-agent" : "your browser info here"}
    r = s.get(url, headers=headers)
#information comes from "form data" tab
login_data = {"login id": "your login",
"password": "your password",
"SignIn":""}
r = s.post(url, data =login_data, headers=headers)
url = "https://theurlyouwanttoaccess.com/myfile.csv"
r = s.get(url)
print(r.content)
