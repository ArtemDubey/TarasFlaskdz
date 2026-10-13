from flask import Flask, jsonify, template_rendered, render_template, request, redirect, url_for


app = Flask(__name__)
app.json.ensure_ascii=False

My_DATA = {
    "name": "Артем",
    "age": 18,
    "city": "Київ(Не точно ще, поки Надвірна)",
    "skills": ["Python", "Flask", "HTML/CSS", "CS2", "Cybersport"]
}
Projects= {
    1: {"title": "Гостьова книга", "description": "Веб-застосунок на Flask для залишення відгуків."},
    2: {"title": "Картка-візитка", "description": "Інтерактивна сторінка-профіль із навичками."},
    3: {"title": "REST API Сервіс", "description": "JSON API для отримання інформації про профіль."}
}
@app.route('/')
def index():
    return render_template('index.html', title="Головна", profile=My_DATA)

@app.route('/about')
def about():
    return render_template('about.html', title="Про мене", profile=My_DATA)

@app.route('/skills')
def skills():
    return render_template('skills.html', title="Навички", profile=My_DATA)

@app.route('/project/<int:id>')
def show_project(id):
    project = Projects.get(id)
    if not project:
        return "Проєкт не знайдено", 404
    return render_template('project.html', project=project)

@app.route('/api/me')
def api_me():
    return jsonify(My_DATA)

if __name__ == '__main__':
    app.run(debug=True, port=5002)