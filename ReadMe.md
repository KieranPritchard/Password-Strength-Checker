# Password Strength Generator

## Project Description

This project is a password strength checker, its purpose is to test passwords to check how effective they are againist guessing/brute-force attacks.

The reason for doing this project, is because I had recently finished doing an online cyber security course. One of the units of the course was about password security, mainly about how to passwords protect infomation. So, i decided in doing this as a project that is related to the infomation I learned about in the course

For this project I decided to use Python, although I want to make a website version of this project in the future. This is part of a few projects related to what I learned during the course.

During this project, there was only really one problem that was promient. This was getting the password strength checked. My first solution was to set four varibles to true/false values which would be checked when a password was inputed however, this proved to be cumbersome. 

My second solution, which is the one in use. It works by using a for loop to check if each character of the password is a number, upper/lower-case letter, or a symbol. Then it appends a number from 1-5 to a list, following this any duplicates are deleted then the final value of the list determines the strength of the password.

## How to Install and Run the Project

## How to Use the Project

## Tests

|Test Input|Test Output|
|---|---|
|abc| Password Strength: Very Weak |
|abc123| Password Strength: Weak |
|Abc123|Password Strength: Moderate |
|Abc123@| Password Strength: Strong|
|A1b2c3d@| Password Strength: Strong|

## Licenses

License is found in the "doc" folder.
