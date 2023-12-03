from flask import Flask, request, jsonify
import smtplib

app = Flask(__name__)

@app.route('/send-email', methods=['GET'])
def send_email():
    email_to = request.args.get('to', '')
    subject = request.args.get('subject', '')
    message = request.args.get('message', '')

    if not email_to or not subject or not message:
        return jsonify({'error': 'Incomplete parameters'}), 400

    # Example: send email using smtplib
    try:
        # SMTP server settings
        smtp_server = 'your_smtp_server'
        smtp_port = 587
        smtp_username = 'your_smtp_username'
        smtp_password = 'your_smtp_password'

        # Create an SMTP connection
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Compose the email
        from_email = 'your_email@example.com'
        to_email = email_to
        subject = subject
        body = message

        email_content = f"Subject: {subject}\n\n{body}"

        # Send the email
        server.sendmail(from_email, to_email, email_content)

        # Close the SMTP connection
        server.quit()

        return jsonify({'success': True, 'message': 'Email sent successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
