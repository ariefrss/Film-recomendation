# Film Recommendation Project

This project allows you to filter movies based on user input, including release year (jadul/modern), rating (memuaskan/biasa aja/buruk), and duration (pendek/sedang/panjang). It uses fuzzy matching to improve the recommendation experience.

## Getting Started

Follow the instructions below to get a local copy of the project up and running on your machine.

### 1. Clone the Repository

First, you need to clone the repository to your local machine. Open your terminal and run the following command:

```bash
git clone git@github.com/ariefrss/Film-recomendation
```

## 2. Open the Project in a Code Editor

Navigate to the project directory and open it in your preferred code editor (such as VS Code or PyCharm):

```bash
cd film-recomendation
```

Then, open the project in your code editor. If you’re using Visual Studio Code, you can use:

```
code .
```

## 3. Create a Virtual Environment

Now, you need to set up a virtual environment to manage the dependencies for this project. Follow these steps:

- Make sure you’re in the root of the project directory (film-recomendation).
- Create a virtual environment by running the following command

```bash
python -m venv venv
```

## After the virtual environment is created, activate it:

- On Windows:

```bash
.\venv\Scripts\activate
```

- On MAC os:

```
source venv/bin/activate
```

You should see the (venv) prefix in your terminal, indicating that the virtual environment is active.

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all the required libraries (like pandas, fuzzywuzzy, etc.) specified in the requirements.txt file.

## Run the Application

Now that everything is set up, you can run the application. In your terminal, make sure you’re still in the project directory and that the virtual environment is activated. Then, run the main.py script:

```bash
python main.py
```

The script will prompt you to enter your search criteria (release year, rating, and duration), and it will show you a filtered list of movies based on the data in the data.csv file.

### File Structure

Here’s a quick overview of the project structure:

```
film-recomendation/
│
├── data.csv               # Dataset containing movie data
├── main.py                # Main script to run the movie recommendation system
├── requirements.txt       # File containing the list of required Python packages
├── README.md              # This file
└── venv/                  # Virtual environment folder (generated after activation)
```

To install these dependencies, run:

```bash
pip install -r requirements.txt
```

## Deactivate the Virtual Environment

When you’re done working on the project, deactivate the virtual environment by running:

```bash
deactivate
```

This will return you to your global Python environment.
