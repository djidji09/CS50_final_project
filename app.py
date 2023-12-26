from website import create_app

# creating the app
app = create_app()

# running the debugger
if __name__ == '__main__':
    app.run(debug=True)
