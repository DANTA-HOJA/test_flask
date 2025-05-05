import json

from flask import Flask, redirect, render_template, request

app = Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)

@app.route("/getSum")
def getSum():
    max = int(request.args.get("max", 100))
    min = int(request.args.get("min", 1))
    result = 0
    for n in range(min, max+1):
        result+=n
    return f"結果：{str(result)}"

@app.route("/en")
def index_en():
    return json.dumps({
            "status": "ok",
            "text": "Hello, flask"
    })

@app.route("/zh")
def index_zh():
    return render_template("index.html", name="小明")
    # return json.dumps({
    #         "status": "ok",
    #         "text": "你好，Flask"
    #     }, ensure_ascii=False)

@app.route("/")
def index():
    print("請求方法：", request.method)
    print("通訊協定：", request.scheme)
    print("主機名稱：", request.host)
    print("路徑：", request.path)
    print("完整的網址：", request.url)
    print("瀏覽器和作業系統：", request.headers.get("user-agent"))
    print("語言偏好：", request.headers.get("accept-language"))
    print("引薦網址：", request.headers.get("referrer"))
    lang = request.headers.get("accept-language")
    if lang.startswith("en"):
        return redirect("/en")
    else:
        return redirect("/zh")

@app.route("/calculate")
def calculate():
    maxNumber = int(request.args.get("max", 0))
    result = 0
    for n in range(1, maxNumber+1):
        result+=n
    return render_template("result_page.html", data=result)

@app.route("/show")
def show():
    name = request.args.get("n", "")
    return f"歡迎光臨，{name}"

@app.route("/page")
def page():
    return render_template("page.html")


@app.route("/data")
def handleData():
    return "My Data"

@app.route("/user/<username>")
def handleUser(username):
    if username == "安安":
        return "你好， " + username
    return "Hello, " + username

app.run(debug=True, port=3000)