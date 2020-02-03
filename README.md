# Python_Question\_Answering\_System

## 1.1 Model requirements
Basic attributes include common attributes such as mailbox, username, and password.

In addition to ordinary users, there should be administrators with special permissions to create users and manage various information.

## 1.2 Functional requirements
Registration and Login: Users log in using their email addresses and passwords, and register using their names, email addresses, and passwords.

View and modify personal information: You can edit personal information, including name, profile, skill level description, etc.

## 1.3 Page requirenments
Login page /login, enter name, email and password to register

Registration page /signup，signup, enter name, email and password to register

Personal homepage /user/，showing the basic user information, you can enter my task list, personal settings page and communication page through this

Profile page /user/edit,
The above requirements are implemented in two modules, one is a user authentication module, and the other is a personal details module.