# Pixelforge
Web application built with Django for generating images from text prompts. Users can input textual prompts, which are processed using pre-trained LLM models to generate corresponding images. The application utilizes Django's framework for handling user input, image generation, and rendering results in real-time.


#  Setup Instructions

## Clone the Repository
Clone the repository to your local machine:

```
git clone <repository-url>
cd <repository-directory>
```

## Setup Virtual Environment (Optional but Recommended)
Create and activate a virtual environment to isolate project dependencies:

```
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate virtual environment (Linux/MacOS)
venv\Scripts\activate  # Activate virtual environment (Windows)
```
## Install Dependencies
Install Python dependencies using pip:

```
pip install -r requirements.txt
```

## Apply Migrations
Apply database migrations to create necessary database tables:

```
python manage.py migrate
```

## Collect Static Files
Collect static files into one directory (if not using a CDN or separate static file storage):

```
python manage.py collectstatic
```
## Run Development Server
Start the Django development server:
```
python manage.py runserver
```
The development server should now be running locally at http://localhost:8000/.


## Usage
Open your web browser and navigate to http://localhost:8000/.
Use the provided forms and interfaces to input text prompts and generate images.


License
This project is licensed under the MIT License - see the LICENSE file for details.


