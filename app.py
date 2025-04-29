
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory employee data (resets when the app restarts)
employees = []

@app.route('/')
def index():
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    position = request.form['position']
    emp_id = len(employees) + 1
    employees.append({'id': emp_id, 'name': name, 'position': position})
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_employee(id):
    global employees
    employees = [emp for emp in employees if emp['id'] != id]
    return redirect('/')

@app.route('/edit/<int:id>', methods=['POST'])
def edit_employee(id):
    name = request.form['name']
    position = request.form['position']
    for emp in employees:
        if emp['id'] == id:
            emp['name'] = name
            emp['position'] = position
            break
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
