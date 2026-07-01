from flask import Flask, render_template, request
from database import get_connection
from encryption import encrypt_data

app = Flask(__name__)

blocked_words = [
    "'",
    "--",
    "DROP",
    "UNION",
    "SELECT"
]

@app.route("/", methods=["GET","POST"])
def home():

    message = ""

    if request.method == "POST":

        username = request.form["username"]
        secret_data = request.form["secret_data"]
        role = request.form["role"]

        for word in blocked_words:

            if word.lower() in username.lower():

                message = "SQL Injection Detected"

                return render_template(
                    "index.html",
                    message=message
                )

        encrypted = encrypt_data(secret_data)

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO users
            (username,secret_data,role)
            VALUES(%s,%s,%s)
            """,
            (
                username,
                encrypted,
                role
            )
        )

        conn.commit()

        cur.close()
        conn.close()

        message = """
        Data Stored Successfully
        | AES-256 Encryption Enabled
        | SQL Injection Protection Enabled
        """

    return render_template(
        "index.html",
        message=message
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )

