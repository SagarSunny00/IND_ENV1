from flask import render_template , Flask 
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('templates/hom.html')

# @app.route('/')
# def index():
#     return render_template('templates/signup.html')

# @app.route('/machine-monitoring')
# def machine_monitoring():
#     # Sample machine data (replace with actual data from your machines)
#     machine1_status = "Running"
#     machine1_temperature = 25
#     machine1_pressure = 10

#     machine2_status = "Idle"
#     machine2_temperature = 20
#     machine2_pressure = 5

#     return render_template('machine_monitoring.html',
#                                machine1_status=machine1_status,
#                                machine1_temperature=machine1_temperature,
#                                machine1_pressure=machine1_pressure,
#                                machine2_status=machine2_status,
#                                machine2_temperature=machine2_temperature,
#                                machine2_pressure=machine2_pressure)

if __name__ == '__main__':
    app.run(debug=True)

# # Sample machine data (replace with actual data from your machines)
# machine1_status = "Running"
# machine1_temperature = 25
# machine1_pressure = 10

# machine2_status = "Idle"
# machine2_temperature = 20
# machine2_pressure = 5

# @app.route('/machine-monitoring')
# def machine_monitoring():
#     return render_template('machine_monitoring.html',
#                                machine1_status=machine1_status,
#                                machine1_temperature=machine1_temperature,
#                                machine1_pressure=machine1_pressure,
#                                machine2_status=machine2_status,
#                                machine2_temperature=machine2_temperature,
#                                machine2_pressure=machine2_pressure)

# if __name__ == '__main__':
#     app.run(debug=True)
