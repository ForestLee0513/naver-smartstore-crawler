from flask import Flask
from src import get_product_info
app = Flask(__name__)

url = "https://smartstore.naver.com/geonlab/products/9031635718"

@app.route('/')
def main():
    print(get_product_info.get_product_info(url))

    return "Everything is good"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=True)
