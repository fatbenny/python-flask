from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
 
# 初始資料
database = {'apple': 5, 'banana': 3, 'orange': 2}

@app.route("/")
def hello_world():
    return "<h1>Hello, World!!</h1>"

# 查詢全部資料
@app.route('/fruit', methods=['GET'])
def fetch():
    app.logger.info("read_collection()")
    return jsonify(database)
# 新增資料
@app.route('/fruit', methods=['POST'])
def create():
    name = request.form.get('name')
    amount = request.form.get('amount')

    if not name or not amount:
        return jsonify({'error': '參數name 和 amount是需要的'}), 400

    try:
        amount = int(amount)  # 轉成數字
    except ValueError:
        return jsonify({'error': 'amount 必須是整數'}), 400

    database[name] = amount
    app.logger.info("create() by Form: name=%s, amount=%d", name, amount)
    return jsonify({'result': '新增成功'})

# 取讀單一資料
@app.route('/fruit/<string:key>', methods=['GET'])
def get(key):
    app.logger.info("read_docu_path('%s') by URL Path.", key)
    if key in database:
        return jsonify({key: database[key]})
    else:
        return jsonify({'result': '查詢失敗'})

# 刪除資料
@app.route('/fruit/<string:key>', methods=['DELETE'])
def delete(key):
    app.logger.info("delete_docu_path('%s') by URL Path.", key)
    if key in database:
        del database[key]
        return jsonify({'result': '刪除成功'})
    else:
        return jsonify({'result': '刪除失敗'})

# 修改資料
@app.route('/fruit/<string:key>', methods=['PUT'])
def update(key):
    data = request.get_json()
    amount = data.get('amount') if data else None
    
    if key in database:
        database[key] = amount
        return jsonify({'result': '更新成功'})
    else:
        return jsonify({'result': '更新失敗'})


if __name__ == "__main__":
    app.run(port=3333, host="0.0.0.0")