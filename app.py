from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
  return "Curio.us AI backend is runing!"

def ask_ai():
  return"Curio.us AI says: Keep Learning!"

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000)
