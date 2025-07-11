﻿# BMI_Analytics
 This project is a simple BMI Calculator with analytics built using Python’s tkinter for GUI and standard libraries like csv, os, and collections. It allows users to enter personal information (Name, Age, Weight, Height), choose between metric or imperial units (kg/m or lb/in), and calculate their BMI. It also stores user data into a CSV file (users_bmidata.csv) and displays real-time analytics like average, highest, lowest BMI, and category distribution. Follow the steps below to set it up on your local machine.
Steps to Set Up and Run the Project
Make sure Python 3.6 or above is installed on your computer. You can check this using:
bash
Copy
Edit
python --version
Clone the repository to your local machine using:
bash
Copy
Edit
git clone https://github.com/your-username/bmi-calculator-analytics.git
cd bmi-calculator-analytics
Ensure the following files exist in the project folder:
main.py – Contains the Tkinter GUI and main application logic
credentials.py – Contains the BMI calculation and categorization functions
analytics.py – Contains CSV export functionality
README.md – Project description and instructions
If any file is missing, create it manually and copy the corresponding code.
Run the application by executing the following command in your terminal:
bash
Copy
Edit
python main.py
The BMI Calculator GUI will launch. Enter Name, Age, Unit, Weight, and Height, then click the “Calculate BMI” button to view results and analytics.
All BMI data will be automatically saved to a file named users_bmidata.csv.
The BMI Analytics section will show:
Total number of users
Average, Highest, and Lowest BMI
Percentage of users in each BMI category
To reset all user data, you can delete users_bmidata.csv:
On Windows:
bash
Copy
Edit
del users_bmidata.csv
On Linux/macOS:
bash
Copy
Edit
rm users_bmidata.csv
Optionally, if you want to manually export user data, use the export_to_csv(users) function from analytics.py.
