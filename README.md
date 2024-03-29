# Laboratory [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

A Python personal python socket server architecture with which you can create your own services.



## Description

The server can manage several clients at the same time. It will respond to client's messages depending on the service called.
Every client can connect to the server. However, a connection process must be followed. If not, the client will be kicked out. Here are the steps to follow:

 - Connect to the server and wait to receive an encoded RSA Pub key.

 - Create a symmetric-key to use for the future exchanges with the server. Encrypt this symmetric-key with the RSA Pub key to send it to the server. (1)

  From now on, every message must end with "\0" and is encrypted with the symmetric-key. (the "\0" is also encrypted)

 - Wait until the server sends you a password request.

 - Send the server's password to the server. (1)

 - Wait until the server sends you a name request.

 - Send your name to the server. (1)

 - Wait until the server sends you the message that you are accepted.

 - Congrats, you are now accepted by the server !

(1) Once the server sends you the last message, you have a limited time to answer it before being kicked out. [See Appendix - Timeout section](#timeout).

The server password is configured in LaboratoryTools/laboratoryTools/network/resources.py [See Appendix - Password section](#password).

The symmetric-key can be an empty string. [See Appendix - Symmetric-key section](#symmetric-key).

Services are not already implements. But it will be soon !!



## Tech Stack

**Server:** Python

**Client Python:** Python, tkinter

**LaboratoryTools:** Python, rsa



## Deployment / Installation

This is a Visual Studio solution containing several projects: Server, Client Python, and LaboratoryTools.

**With Visual Studio:** The solution is configured to launch the Server and the Client Python project in debug mode. Internal dependencies are already managed by Visual Studio.
**Without Visual Studio:** You need to copy LaboratoryTools/laboratoryTools folder in Server and/or Client folder depending on which project you want to run. Then, you can run it.



## First usage

The first time you launch the Server.py or the Client_Python.py program, you may need:
- An internet connection.
- Python3 package installer PIP3.
- **For linux user:** root privileges.



## External Dependencies

Each of the two programs (Server.py, Client_Python.py) depends on laboratoryTools package in LaboratoryTools project. All other external dependencies are managed by the \_\_init\_\_.py file in the above package. For now, two modules need to be installed in addition to the Python's standard library:

- rsa (can be installed with pip.)
```bash
pip install rsa
```

- tkinter (Installed with Python's standard library for Windows. May required an installation for Linux.)

```bash
sudo apt install python3-tk
```

If those packages are not available, Server.py or Client_Python.py program will try to install them automatically.



## Appendix


### Timeout
The timeout for the connection process is configured in LaboratoryTools/laboratoryTools/network/socket.py in ServerSocket class or the super class. If the symmetric-key generation takes too much time, you probably should generate it before trying to connect to the server.


### Password
The server's password is configured in LaboratoryTools/laboratoryTools/network/resources.py. In order to secure the server, it is very important not to leave the default password and to change it. Also, the password must not be an empty string.


### Symmetric-key
This key generated by the client is used to encrypt messages with the server after the first exchange with the RSA Public key. The symmetric encryption/decryption process must be defined in LaboratoryTools/laboratoryTools/securityManager/core.py file in SecurityManager class methods. For now, the key can not be modified once it is sent to the server. It is possible to use an empty string as a key. In this case, messages between the server and the client will not be encrypted anymore. By consequence, anyone can read them with a network analyzer (/!\ This is the default behavior until you have defined your own encryption/decryption behavior /!\\).

NB: To improve your server security, you should define your own symmetric encryption/decryption but never push it on any VCS. This is the reason why there is not a real encryption/decryption mechanic but only a default non secured one. I recommend you to use this git command to ignore changes in the tracked file:

```bash
git update-index --skip-worktree LaboratoryTools/laboratoryTools/securityManager/core.py
```


### Name

Both the server and the client must have a name. Those names are not a real identifier: two clients can have the same name as well as the server and a client. They are only used to make socket connection more human readable. So, the only real way to identify a connection is to look at the combination (IP Address, Port). Once a client is accepted by the server, it can send a name request at any time. For now, the client name can not be modified once it is sent to the server.



## Disclaimer

I do not pretend to be a cyber security expert. So, even if I tried to secure the server in different ways, keep in mind this is not a total protection against hackers. Hence, be really careful with the data you exchange between the server and the clients. 

Having say this, feel free to give me some feedback as mentioned in [Feedback section](#feedback).



## Roadmap

- Use JSON format for exchanges between the server and the clients. (Soon)
- Change of message display in tkinter window for Client_Python.py program. (Soon)
- Block IP address when a client try to connect but don't pass the connection process. (Soon)
- Enable symmetric-key modification. (Soon)
- Enable name modification. (Soon)
- Create the Echo service. (Soon)
- Create the Chat service. (Soon)
- Create an Android Client app - on an other repo, I will put the link here when it will be available. (Not so soon)
- Create a C++ Client. (Really not so soon)
- Create the HTTP Service.



## Related

Android Client app. (Not vailable yet)



## Authors

- [@GillouH](https://www.github.com/GillouH)



## Feedback

Feel free to [contact me by email](#support) if you have some constructive remarks, advices, and requests concerning the evolution of the project and its features. I will answer you with pleasure !



## Acknowledgements
I would like to thank those who helped me to write and correct this README.md in addition to:
- [Oliver Jumpertz](https://twitter.com/oliverjumpertz) for [his tweet](https://twitter.com/oliverjumpertz/status/1425061034465845248) about minimum requirements list to have in a README.md
- [Katherine Peterson](https://twitter.com/katherinecodes) for her really usefull README.md [editor](https://readme.so/)
- [Samina](https://twitter.com/saminacodes) for sharing both of them in this [tweet](https://twitter.com/saminacodes/status/1425197925785763842) and for all her coding content.



## Support

For support, email me at gilles.hubert97@gmail.com.