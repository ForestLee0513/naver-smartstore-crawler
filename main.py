from flask import Flask, request, jsonify
from src import get_product_info
app = Flask(__name__)

@app.route("/get-products")
def get_products():
    data = request.json
    product_info_list = []

    # data.url의 형식이 리스트가 아닐 경우 에러 반환
    if type(data['url']) != list:
        return "Invalid request, please check document."
    
    for product_url in data['url']:
        product_info_list.append(get_product_info.get_product_info(product_url))
    
    return jsonify({
        "productInfo": product_info_list
    })

@app.route('/')
def main():
    return "NAVER Smartstore crawler is running.."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=True)
