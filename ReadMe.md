# Password Strength Checker

<div align="center">
    <img alt="GitHub Created At" src="https://img.shields.io/github/created-at/KieranPritchard/Password-Strength-Checker">
    <img alt="GitHub License" src="https://img.shields.io/github/license/KieranPritchard/Password-Strength-Checker">
    <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/t/KieranPritchard/Password-Strength-Checker">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/KieranPritchard/Password-Strength-Checker">
    <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/KieranPritchard/Password-Strength-Checker">
    <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/KieranPritchard/Password-Strength-Checker">
</div>

## Project Description

This project is a password strength checker, its purpose is to test passwords to check how effective they are againist guessing/brute-force attacks.

The reason for doing this project, is because I had recently finished doing an online cyber security course. One of the units of the course was about password security, mainly about how to passwords protect infomation. So, i decided in doing this as a project that is related to the infomation I learned about in the course

For this project I decided to use Python, although I want to make a website version of this project in the future. This is part of a few projects related to what I learned during the course.

During this project, there was only really one problem that was promient. This was getting the password strength checked. My first solution was to set four varibles to true/false values which would be checked when a password was inputed however, this proved to be cumbersome. 

My second solution, which is the one in use. It works by using a for loop to check if each character of the password is a number, upper/lower-case letter, or a symbol. Then it appends a number from 1-5 to a list, following this any duplicates are deleted then the final value of the list determines the strength of the password.

## How to Use the Project

1. **Clone The Repository:**

   Download the project to your local device, this can be done with git.
   
3. **Run The Program:**

   Navigate to the directory that the project is stored and run the script in the terminal.
   
4. **Input Your Password:**

   When you run the program, you will see a prompt. Type in the password you want to check and hit enter.
   
5. **View The Password Strength:**

   The program then analyses the password and display its strength.
   Strength catagorys include:
   * "Very Weak"
   * "Weak"
   * "Moderate"
   * "Strong"
   * "Very Strong"
   
6. **Check Again:**

   in order to check another password, all you have to do is run the program again.

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
