from __init__ import app
app.secret_key="secret"

if __name__ == "__main__":
    app.debug = True
    app.run()
