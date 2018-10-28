from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get_classifier_result/<version>", methods=['GET', 'POST'])
def return_classifier_result(version):
    if request.method == 'POST':
        if int(version) == 1:
            return jsonify(version = 1, predict = request.get_json()['predict'])
        else:
            return jsonify(version = 0, predict = request.get_json()['old_predict'])

@app.route("/")
def hello():
    return """Привет я flask сервер
    Отправь мне POST запрос на url /get_classifier_result/<version>
    Если хочешь использовать старую версию, то подставь 0,
    а если новую, то 1 ;)
    Также отправь мне json в формате 
    {"predict" : i} для новой версии и 
    {"old_predict": i} для старой.
    В ответ я тоже отправлю тебе json в таком формате:
    {"version" : value, "predict" : value}
    """

if __name__ == "__main__":
    app.run()
