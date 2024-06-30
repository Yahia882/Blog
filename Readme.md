# My Blog Web App

## Overview

My Blog Web App using Django is a simple monolithic web application designed for users to read and save blog posts. The application is built with an integrated architecture, combining both the frontend and backend into a single cohesive unit. This README file provides an overview of the features and functionalities of the web app.

## Features

- **Monolithic Architecture**: The entire application, including both frontend and backend, is built as a single unit, ensuring tight integration and ease of deployment.
- **Read Later Functionality**: Users can save blog posts to read later using cookies. The "Read Later" button changes color when pressed and the post is added to the Read Later page.
- **Admin Posting**: Blog posts are created and managed by admin users.
- **Image Uploads**: Admin users can upload images to be associated with blog posts.
- **ORM for Database Interaction**: We use an Object-Relational Mapping (ORM) system to interact with the database, simplifying database operations.

## Pages

1. **Home Page**: The landing page of the web app, featuring a welcome message and navigation links.
2. **All Posts Page**: Displays a list of all blog posts. Users can browse through all available posts.
3. **Read Later Posts Page**: Shows posts that the user has saved to read later. This is managed using cookies.
4. **Post Details Page**: Displays the full content of a selected blog post, along with comments.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Yahia882/Blog.git
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run migrations**:
    ```sh
    python manage.py migrate
    ```

4. **Create a superuser for admin functionalities**:
    ```sh
    python manage.py createsuperuser
    ```

5. **Start the development server**:
    ```sh
    python manage.py runserver
    ```

6. **Access the application**:
    Open your web browser and navigate to `http://localhost:8000`.

## Usage

- **Home Page**: Welcome page with navigation links.
- **All Posts Page**: Browse all blog posts. Click on a post to view its details.
- **Read Later**: Click the "Read Later" button on any post to save it using cookies. The button will change color to indicate that the post has been saved. Access your saved posts from the "Read Later" page.
- **Post Details Page**: View the full content of a post and read comments.
- **Admin**: Login as an admin user to create, edit, or delete posts and upload images for posts.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



