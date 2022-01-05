# Like Reddit Backend Clone

Fully functional forum backend api that can be integrated with any frontend, there are many features for the admin to manage his forum and user to have a good experience.

## Features

NOTE: **Every thing published is a post and contain all post feature whatever it was thread, comment or replay.**

- post features
  - CRUD functions
  - report post
  - save post
  - upvote / downvote on post
  - react with emojis on post
- thread features
  - CRUD functions
  - make it private for premium users
  - user can comment on thread
  - user can replay on comment
  - user can change privacy (public/private)
- notification features
  - user can follow threads
  - list all notifications
- user features
  - follow another user
  - karma system (points for reputation)
- admin features
  - CRUD feature for existing categories/sub-categories
  - add emojis that user allowed to use
  - make user premium
  - make user verified
  - make user ban for specific period
  - [ ] send different types of notification to all users (popup / banner / etc...)
- auth features
  - basics (login/register/logout)
  - login using JWT
  - verification mail on register
  - forget password function with verification mail
  - and more...

## Built With

- [django](https://www.djangoproject.com/)
- [rest framework](https://www.django-rest-framework.org/)

## Getting Started

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

- python 3.9+
- create virtual env

### Installation

1. Clone the repo **inside the virtual env**.

   ```sh
   git clone https://github.com/mohamed17717/Like-Reddit-Backend-Clone
   ```

2. Install packages

   ```sh
   pip install -r requirements.txt
   ```

3. migrate the database

   ```sh
    python manage.py makemigrations
    python manage.py migrate
   ```

4. run server

   ```sh
   python manage.py runserver
   ```

5. start test it with postman files attached _(optional)_

## Online Resources

- [postman workspace](https://www.postman.com/mhmd17/workspace/little-reddit-api)

## TODO

- [ ] update is_private property in post to is_premium
- [ ] in thread view user got twice from thread and post split that
- [ ] use uuid and slug instead of pk
- [ ] new notification type to pin message as a banner in pages
- [ ] api to merge thread
- [ ] abstract class for soft_delete
- [ ] extra fields like (user: bio, gender, interests, ...)
- [ ] generate url for report post type and generate in sub types url
- [ ] make report decision affect places automatic (notify, hide post or whatever)
- [ ] post contain emoji list with their url

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact

Mohamed Mahmoud - [LinkedIn](https://linkedin.com/in/mohamed17717/) - d3v.mhmd@gmail.com
