# Question 7:

## **What does the server say**

Checking if port is open or not? 

```powershell
chandrabhan@cicada3301:~$ nc -zvnw 1 139.59.26.242 20632
Connection to 139.59.26.242 20632 port [tcp/*] succeeded!
chandrabhan@cicada3301:~$ 
```

Screenshot: 

![Untitled](/attachments/Q72.png)

Listening to port:

```powershell
chandrabhan@cicada3301:~$ nc  139.59.26.242 20632
HTTP/1.1 200 OK
Content-Type: text/plain

CTF{m0r3_7r0ubl3_7h4n_175_w0r7h}

Welcome to the Systems induction CTF. If at first you don't see anything, look harder
Welcome to the Systems induction CTF. If at first you don't see anything, look harder
Welcome to the Systems induction CTF. If at first you don't see anything, look harder
Welcome to the Systems induction CTF. If a^c

chandrabhan@cicada3301:~$ 
```

Screenshot: 

![Untitled](/attachments/Q71.png)