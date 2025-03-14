from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return """
    <html>
        <head>
            <style>
                p {
                    color: blue;
                    font-size: 20px;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to My Homepage!</h1>
            <p>This is built with Flask.</p>
        </body>
    </html>
    """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

