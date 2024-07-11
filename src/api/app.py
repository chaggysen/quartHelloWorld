import os
from bootstrapper import initialize_app

app = initialize_app()

if  __name__  ==  '__main__':
  port  =  int(os.environ.get("PORT", 8080))
  app.run(host='0.0.0.0', port=port)