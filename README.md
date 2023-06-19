# Simple HTML Forms x Display with Flask

This project demonstrates the use of HTML forms for collecting user input and displaying the entered data on a separate page. It also includes a salary breakdown displayed in the form of a pie chart.

## Project Structure

The project consists of the following files:

- `index.html`: The main HTML file that contains the form for collecting user input.
- `display.html`: The HTML file that displays the entered data and salary breakdown.
- `app.py`: Python script for handling form submission and generating an Excel file.

## Python Setup and Dependencies Installation

1. Make sure you have Python 3 installed on your system.
2. Install the required Python packages by running the following command:
3. Installing Dependencies
 
    ```pip install flask pandas openpyxl ```

    or 
    
    ```pip install -r requirements.txt ```

## Running the Application

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Start the Flask development server by running the following command:
    
    ```pip install app.py ```
4. Open a web browser and go to `http://localhost:5000`.
5. Fill in the required information in the form fields and submit the form.
6. You will be redirected to the `display.html` page, where the entered data will be displayed along with the salary breakdown pie chart.
7. The submitted data will also be saved to an Excel file named `form_data.xlsx` in the project directory.