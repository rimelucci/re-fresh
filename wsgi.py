from __init__ import app

if __name__ == "__main__":
    app.debug = True
    app.secret_key="secret"
    app.run()
