# Idor-Hunter
**Python Script to Find Idor Vulnerabilities**

This script is based in Autorize Extension from BurpSuite

https://github.com/Quitten/Autorize


**How it Works?**

This script has very simple operations:

#1 Step:

Send a request to the URL that the user has indicated with the user's cookie.
Capture the response code and its Content-Length.

#2 Step:

It sends a request without a cookie and captures the response code and the Content-Lenght, to compare if the response is the same as with an authorized cookie.

#3 Step:

It sends one last request but with the modified cookie to check if the target verifies the cookie it receives.

#4 Step:

Finally, it will compare the answers and tell you the result.


**Installation**

git clone https://github.com/S12cybersecurity/Idor-Hunter

pip3 install requests

pip3 install argparse


**Usage**

Basic Usage:

python3 idor_hunter.py --url URL --cookie "Cookie: COOKIE"

![image](https://user-images.githubusercontent.com/79543461/171822048-599cce83-656b-4a3e-9cb6-a02527db2545.png)

With Proxy:

python3 idor_hunter.py --url URL --cookie "Cookie: COOKIE" --proxy http://127.0.0.1:8080

![image](https://user-images.githubusercontent.com/79543461/171822595-3589d42e-1ff1-4079-8b36-0c3a0a910509.png)




