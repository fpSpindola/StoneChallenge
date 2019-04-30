from api.factory import create_app

if __name__ == '__main__':
    app, config = create_app()
    app.run()
