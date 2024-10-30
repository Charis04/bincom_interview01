from flask import Flask, render_template, request
import pymysql


app = Flask(__name__)

DB_CONFIG = {
    'host': 'localhost',
    'user': 'charis',
    'password': 'ayanfeoluwa',
    'db': 'bincomtest',
    'cursorclass': pymysql.cursors.DictCursor  # To fetch results as dictionaries
}

def get_db_connection():
    """Establishes a connection to the MySQL database."""
    connection = pymysql.connect(**DB_CONFIG)
    return connection

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    try:
        # Connect to the database
        connection = get_db_connection()
        with connection.cursor() as cursor:
            # Write a query to retrieve data from your table
            cursor.execute("SELECT * FROM announced_pu_results")
            results = cursor.fetchall()  # Fetch all results
            cursor.execute("SELECT uniqueid, polling_unit_name FROM polling_unit WHERE uniqueid BETWEEN 8 AND 27 ORDER BY polling_unit_name ASC")
            polling_u = cursor.fetchall()

    finally:
        connection.close()

    polling_uid = request.form.get("polling_uid")
    polling_uid = str(polling_uid)

    return render_template('home.html', data=results, polling_u=polling_u, polling_id=polling_uid)

if __name__ == "__main__":
    app.run(debug=True)
