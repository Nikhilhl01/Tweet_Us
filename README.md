# TweetUs

TweetUs is a dynamic web platform designed for seamless social interaction, allowing users to share their thoughts and moments through tweets. Built with Django, TweetUs offers robust features, including user authentication, the ability to create tweets with images, and options to edit, delete, and like posts. Experience a streamlined and engaging way to connect and share on a user-friendly platform that brings your ideas to life.

## Features

- **User Authentication**: Secure login and registration system.
- **Tweet Management**: Users can create, edit, delete, and like tweets.
- **Image Support**: Tweets can include images.
- **Security**: CSRF tokens are used to protect against cross-site request forgery.

## Technologies Used

- **Frontend**: HTML, Bootstrap
- **Backend**: Django
- **Security**: CSRF tokens, Django authentication system

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Nikhilhl01/TweetUs.git
   
2. Navigate to the project directory:
   ```bash
   cd TweetUs
   
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   
4. Run the development server:
   ```bash
   python manage.py runserver


## Usage
-Visit the homepage to create an account or log in.<br>
-After logging in, you can create a tweet that includes an image.<br>
-Edit or delete your tweets as needed, like other users' tweets.<br>


## Security
-This application uses Django's built-in authentication system to manage user sessions. Additionally, CSRF tokens are implemented to protect forms from cross-site request forgery attacks.
