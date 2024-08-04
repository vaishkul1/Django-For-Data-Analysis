# CSV Analyzer

CSV Analyzer is a Django-based web application that allows users to upload CSV files, perform data analysis, and visualize the results. Users can view the first few rows of their data, summary statistics, handle missing values, and generate histograms for visualization.

# Features

- Upload CSV files for analysis.
- Display the first five rows of the data.
- Show summary statistics (mean, median, standard deviation) for numeric columns.
- Identify and handle missing values by dropping rows with missing values.
- Generate histograms for data visualization.

# Setup Instructions

Follow these steps to set up the project on your local machine:

# Prerequisites

- Python 3.7 or higher
- Django 3.0 or higher
- Git
- pip

# Installation

1. Clone the Repository
   git clone https://github.com/vaishkul1/Django-For-Data-Analysis.git
   cd csv-analyzer

2. Activate a Virtual Environment:
   On mac use: source venv/bin/activate  
   On Windows use: venv\Scripts\activate

   ```

   ```

3. Install Dependencies:
   pip install -r requirements.txt
   This step will install all the required libraries in the project.

4. Run Migrations:
   python manage.py migrate

5. Run the Development Server:
   python manage.py runserver

6. Open the Application in Your Browser:
   - Navigate to `http://127.0.0.1:8000` in your web browser.

# Brief Explanation

This CSV Analyzer project consists of a Django application that provides a user interface for uploading CSV files, processing data, and visualizing the results.

# index.html:

The home page where users can upload CSV files.

# process.html:

Displays the first five rows of data, summary statistics, missing values, and handles missing values by dropping rows.

# visualize.html:

Displays histograms of the data.

The views in "views.py" handle the logic for reading CSV files, processing data, and generating visualizations. The "static/css/styles.css" file contains styles to improve the appearance of the web pages.

# Note:

- Ensure that the uploaded files are in CSV format.
- The application uses the messages framework to display feedback to the user.
- The project uses Matplotlib for generating histograms.
