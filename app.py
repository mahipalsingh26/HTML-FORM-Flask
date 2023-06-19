from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os.path


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get the form data
    full_name = request.form.get('fullName')
    contact = request.form.get('contact')
    email = request.form.get('email')
    current_company = request.form.get('currentCompany')
    company_type = request.form.get('companyType')
    sector = request.form.get('sector')
    industry = request.form.get('industry')
    currency = request.form.get('currency')
    allowance = request.form.get('allowance')
    bonus = request.form.get('bonus')
    total_annual = request.form.get('totalAnnual')

    data = {
        'Full Name': [full_name],
        'Contact': [contact],
        'Email': [email],
        'Current Company': [current_company],
        'Company Type': [company_type],
        'Sector': [sector],
        'Industry': [industry],
        'Currency': [currency],
        'Allowance': [allowance],
        'Bonus': [bonus],
        'Total Annual': [total_annual]
    }

    # Check if the Excel file already exists
    if os.path.isfile('form_data.xlsx'):
        # Load the existing data from the file
        existing_data = pd.read_excel('form_data.xlsx')
        # Concatenate the existing data with the new form data
        updated_data = pd.concat([existing_data, pd.DataFrame(data)], ignore_index=True)
        # Save the updated data to the Excel file
        updated_data.to_excel('form_data.xlsx', index=False)
    else:
        # Create a new DataFrame with the form data
        df = pd.DataFrame(data)
        # Save the DataFrame to an Excel file
        df.to_excel('form_data.xlsx', index=False)

    # Redirect to the display page with form data as query parameters
    return redirect(url_for('display', fullName=full_name, contact=contact, email=email,
                            currentCompany=current_company, companyType=company_type,
                            sector=sector, industry=industry, currency=currency, allowance=float(allowance),
                            bonus=float(bonus), totalAnnual=float(total_annual)))

@app.route('/display')
def display():
    return render_template('display.html')

if __name__ == '__main__':
    app.run(debug=True)
