import os
from bootstrapper import initialize_app

app = initialize_app()

@app.route('/')
async def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
