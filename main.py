from website import create_app

app = create_app()

if __name__ == "__main__":
  # When making changes to python code this automatically reruns the web server
  app.run(debug=True) 