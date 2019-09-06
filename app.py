from flask import Flask, render_template
import os


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/page2")
def page2():
    return render_template("page2.html")

@app.route("/page3")
def page3():
    return render_template("page3.html")


dic = {
"smari":["smári", "0601992809"],
"einar":["einar", "1234567890"]
}



@app.route("/a")
def a():
    smari=dic["smari"][0]
    smarikt=dic["smari"][1]
    einar=dic["einar"][0]
    einarkt=dic["einar"][1]

    return render_template("a.html", sss=smari, ssskt=smarikt, ein=einar, einkt=einarkt)

@app.route("/sida")
def villa():
    return"""
    <h1>þessi síða fannst ekki</h1>
    """

@app.route("/sida/<kennitala>")
def sida(kennitala):
    print(kennitala)
    if kennitala.isnumeric() != True:
        return"""
        <h1>þessi síða fannst ekki</h1>
        """
    sum = 0
    for i in kennitala:
        sum = sum + int(i)

    else:
        return render_template("sida.html",summa=sum, kt=kennitala)

news = {
"bio_1":
        {
        "titill":"Kalli á þakinu",
        "mynd":"https://kvikmyndir.is/images/poster/2644_500.jpg",
        "grein":"kalli á þakinu er mynd um strák sem lifir á þaki og er með kúl hatt",
        "hofundur":"smarikul@hotmail.com"
        },
"bio_2":
        {
        "titill":"Toy story",
        "mynd":"https://kvikmyndir.is/images/poster/x301_300.jpg.pagespeed.ic.UxauuP6dsC.webp",
        "grein":"leikföngin hanns adda lyfna við og fara á úrskeiðum og lenda í alskonar vesni og ævintírum",
        "hofundur":"einar@hotmail.com"
        },
"bio_3":
        {
        "titill":"Monster hf",
        "mynd":"https://kvikmyndir.is/images/poster/2053_500.jpg",
        "grein":"skrímslin Mike og Sully fara á kostum þegar þeir þurfa koma stelpu sem slapp inn í skrímsla heiminn aftur heimtilsín ",
        "hofundur":"smari@hotmail.com"
        },
"bio_4":
        {
        "titill":"leitin af nemo",
        "mynd":"https://kvikmyndir.is/images/poster/2550_500.jpg",
        "grein":"marel hef tínt soni sínum nemo og þarf nú að leita að honum",
        "hofundur":"einar@hotmail.com"
        },
}

@app.route("/bio")
def b():
    return """<h1>tóm síða</h1>"""

@app.route("/bio/b1")
def b1():
    return render_template("b1.html")


@app.route("/bio/<news_number>")
def b_page(news_number):
    new = None
    if news_number in news:
        new = news[news_number]
        return render_template("b.html", new=new)
    else:
        return "villa"








if __name__ == "__main__":
    app.run()
    app.run(debug=True, use_reloader = True)
