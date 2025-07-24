from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'f3956c777cebc566ffb95408917364c2'  # Required for flashing messages

# === Mail Configuration ===
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'v9630094@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'rtwt opco zptt jwvz'  # Use Gmail App Password

mail = Mail(app)

# === Home Page ===
@app.route('/')
def index():
    return render_template('form.html')

# === Handle Form Submission ===
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    phone = request.form.get('phone')
    interest = request.form.get('interest')

    if name and phone and interest:
        try:
            msg = Message("New Interest Submitted - ThinkData AI",
                          sender='tdaitech@gmail.com',
                          recipients=['tdaitech@gmail.com'])
            msg.body = f"Name: {name}\nPhone: {phone}\nInterest: {interest}"
            mail.send(msg)
            flash("✅ Your interest is submitted.", "success")
        except Exception as e:
            print(str(e))
            flash("❌ There was a problem submitting your interest. Please try again later.", "danger")
    else:
        flash("❗Please fill all the fields.", "warning")

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

