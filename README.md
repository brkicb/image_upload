# Image Upload Tutorial

This is a simple project that demonstrates how you could upload an image from a Next.js frontend into a Django backend.

In order to test out this project, follow these steps:

-   clone the repository
-   in the frontend folder, run: npm install, this will install the required frontend packages
-   in the frontend folder, run: npm run dev, this will run your frontend on localhost:3000
-   in the backend folder, run: python3 -m venv venv
-   then activate the virtual environment (MacOS: source venv/bin/activate, Windows: .\venv\Scripts\activate)
-   in the backend folder, run: pip install -r requirements.txt
-   then in the backend run: python manage.py migrate
-   then after that run: python manage.py runserver

Then under backend/image_upload/settings.py:

-   under DATABASES, set the NAME and PASSWORD field to your PostgreSQL database
