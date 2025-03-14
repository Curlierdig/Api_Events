from app import create_app
# llama a la funcion create_app del modulo app/__init__.py
app = create_app()

if __name__ == "__main__":
    app.run(port=4000, debug=True)