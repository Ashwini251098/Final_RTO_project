from flask import Flask, render_template, request
import cx_Oracle
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rto', methods=['POST'])
def submit_form():
    print(request.method)
    if request.method == 'POST':
        print("POST API received successfully")
        registerNo = request.form['registerNo']
        firstname = request.form['firstname']
        lastName = request.form['lastName']
        age = request.form['age']
        modelName = request.form['modelName']
        modelYear = request.form['modelYear']
        manufacturedDate = request.form['manufacturedDate']
        registered_date = datetime.strptime(request.form['registeredDate'], '%Y-%m-%d')

        try:
            con = cx_Oracle.connect('FTP812ATMTest2/password123@100.76.152.215:1521/EPM19CPDB')
            cursor = con.cursor()

            cursor.execute("SELECT * FROM vehicle_details")
            rows = cursor.fetchall()
            for row in rows:
                print(row)

            cursor.execute("""
                INSERT INTO vehicle_details (registerNo, firstName, lastName, age, modelName, modelYear, manufacturedDate, Registered_date)
                VALUES (:rto_register_no, :first_name, :last_name, :age, :model_name, :model_year, :manufactured_date, :registered_date)
            """, {
                'rto_register_no': registerNo,
                'first_name': firstname,
                'last_name': lastName,
                'age': age,
                'model_name': modelName,
                'model_year': modelYear,
                'manufactured_date': manufacturedDate,
                'registered_date': registered_date
            })
            con.commit()

            cursor.execute("""
                SELECT * FROM (
                    SELECT * FROM vehicle_details ORDER BY REGISTERNO DESC
                ) WHERE ROWNUM = 1
            """)

        except cx_Oracle.DatabaseError as e:
            error_msg = "Error connecting to the database: {}".format(str(e))
            return error_msg
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'con' in locals():
                con.close()

    # After submitting the data
    return 'Your Vehicle got registered successfully!'

@app.route('/script')
def script():
    return render_template('script.js')

if __name__ == '__main__':
    app.run(debug=True)
