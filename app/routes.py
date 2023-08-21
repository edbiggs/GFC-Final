from flask import render_template, request, redirect, url_for, flash
from app import app
from .forms import SignUpForm, LoginForm, SearchForm, AddForm
import requests
import json
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Van, db
from werkzeug.security import check_password_hash
from urllib.parse import urlencode
import pandas as pd


data = pd.read_csv('van_data.csv', index_col=0)
data_dict = data.to_dict()
df = pd.DataFrame(data_dict)
df_rows = df.iterrows()

van_info = [row for row in df_rows]


@app.route('/', methods=["GET", "POST"])
def home_page():

    print(Van.query.all())

    return render_template('index.html', tables=[df.to_html()], titles=[''], vans=df_rows)


@app.route('/login', methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            password = form.password.data

            user = User.query.filter_by(username=username).first()

            if user:
                if check_password_hash(user.password, password):
                    login_user(user)
                    return redirect(url_for('home_page'))
                else:
                    print("Error: Username or password invalid")
            else:
                print(f"Could not find user {user}")

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout_page():
    logout_user()
    return redirect(url_for('login_page'))


@app.route('/vans/', methods=["GET", "POST"])
def vans_page():

    van_count = range(len(van_info))

    vans = []

    last_milage = []

    last_oil_change_milage = []

    last_oil_change_date = []

    last_front_tire_change_date = []

    last_rear_tire_change_date = []

    last_trans_fluid_change_milage = []

    last_battery_change_date = []

    last_air_filter_change_milage = []

    last_spark_plug_change_milage = []

    last_coil_change_milage = []

    last_state_inspection_date = []

    last_emissions_date = []

    last_front_brake_change_milage = []

    last_rear_brake_change_milage = []

    plate = []

    vin = []

    model = []

    notes = []

    active = []

    for i in van_count:
        vans.append(van_info[i][0])

        last_milage.append(van_info[i][1][0])

        last_oil_change_milage.append(van_info[i][1][1])

        last_oil_change_date.append(van_info[i][1][2])

        last_front_tire_change_date.append(van_info[i][1][3])

        last_rear_tire_change_date.append(van_info[i][1][4])

        last_trans_fluid_change_milage.append(van_info[i][1][5])

        last_battery_change_date.append(van_info[i][1][6])

        last_air_filter_change_milage.append(van_info[i][1][7])

        last_spark_plug_change_milage.append(van_info[i][1][8])

        last_coil_change_milage.append(van_info[i][1][9])

        last_state_inspection_date.append(van_info[i][1][10])

        last_emissions_date.append(van_info[i][1][11])

        last_front_brake_change_milage.append(van_info[i][1][12])

        last_rear_brake_change_milage.append(van_info[i][1][13])

        plate.append(van_info[i][1][14])

        vin.append(van_info[i][1][15])

        model.append(van_info[i][1][16])

        notes.append(van_info[i][1][17])

        active.append(van_info[i][1][18])

    # WHY IS INDEX OUT OF RANGE?!
    # print(len(vans))

    # print(len(last_milage))

    # print(len(last_oil_change_milage))

    # print(len(last_oil_change_date))

    # print(len(last_front_tire_change_date))

    # print(len(last_rear_tire_change_date))

    # print(len(last_trans_fluid_change_milage))

    # print(len(last_battery_change_date))

    # print(len(last_air_filter_change_milage))

    # print(len(last_spark_plug_change_milage))

    # print(len(last_coil_change_milage))

    # print(len(last_state_inspection_date))

    # print(len(last_emissions_date))

    # print(len(last_front_brake_change_milage))

    # print(len(last_rear_brake_change_milage))

    # print(len(plate))

    # print(len(vin))

    # print(len(model))

    # print(len(notes))

    # print(len(active))
    # print([i for i in range(len(van_info))])

    if Van.query.all() == []:
        for i in van_count:

            Van.van_number = vans[i]

            Van.milage = last_milage[i]

            Van.last_oil_change_milage = last_oil_change_milage[i]

            Van.last_oil_change_date = last_oil_change_date[i]

            Van.last_front_tire_change_date = last_front_tire_change_date[i]

            Van.last_rear_tire_change_date = last_rear_tire_change_date[i]

            Van.last_trans_fluid_change_milage = last_trans_fluid_change_milage[i]

            Van.last_battery_change_date = last_battery_change_date[i]

            Van.last_air_filter_change_milage = last_air_filter_change_milage[i]

            Van.last_spark_plug_change_milage = last_spark_plug_change_milage[i]

            Van.last_coil_change_milage = last_coil_change_milage[i]

            Van.last_state_inspection_date = last_state_inspection_date[i]

            Van.last_registration_renewal_date = last_emissions_date[i]

            Van.last_front_brake_change_milage = last_front_brake_change_milage[i]

            Van.last_rear_brake_change_milage = last_rear_brake_change_milage[i]

            Van.plate = plate[i]

            Van.vin = vin[i]

            Van.van_model = model[i]

            Van.notes = notes[i]

            Van.active = active[i]

            van_class_info = Van(Van.van_number, Van.milage, Van.last_oil_change_milage, Van.last_oil_change_date, Van.last_front_tire_change_date, Van.last_rear_tire_change_date, Van.last_trans_fluid_change_milage, Van.last_battery_change_date, Van.last_air_filter_change_milage,
                                 Van.last_spark_plug_change_milage, Van.last_coil_change_milage, Van.last_state_inspection_date, Van.last_registration_renewal_date, Van.last_front_brake_change_milage, Van.last_rear_brake_change_milage, Van.plate, Van.vin, Van. van_model, Van.notes, Van.active)
            print(van_class_info)
            db.session.add(van_class_info)
            db.session.commit()

    data = [van.to_dict() for van in Van.query.all()]

    return render_template('vans.html', data=data)


@app.route('/data', methods=["GET"])
def get_data():
    data = Van.query.order_by(Van.van_number)
    return {
        'status':'Ok',
        'data':[van.to_dict() for van in data]
    }


@app.route('/data', methods=['POST'])
def update():
    data = request.get_json()
    if 'id' not in data:
        return 'error: van info not found'
    van = Van.query.get(data['id'])

    for field in ['van_number',
                'milage',
                'last_oil_change_milage',
                'last_oil_change_date',
                'last_front_tire_change_date',
                'last_rear_tire_change_date',
                'last_trans_fluid_change_milage',
                'last_battery_change_date',
                'last_air_filter_change_milage',
                'last_spark_plug_change_milage',
                'last_coil_change_milage',
                'last_state_inspection_date',
                'last_registration_renewal_date',
                'last_front_brake_change_milage',
                'last_rear_brake_change_milage',
                'plate',
                'vin',
                'van_model',
                'notes',
                'active']:
        if field in data:
            setattr(van, field, data[field])
    db.session.commit()
    return '', 204


# vans=vans, last_milage=last_milage, last_oil_change_milage=last_oil_change_milage, last_oil_change_date=last_oil_change_date, last_front_tire_change_date=last_front_tire_change_date, last_rear_tire_change_date=last_rear_tire_change_date, last_trans_fluid_change_milage=last_trans_fluid_change_milage, last_battery_change_date=last_battery_change_date, last_air_filter_change_milage=last_air_filter_change_milage, last_spark_plug_change_milage=last_spark_plug_change_milage, last_coil_change_milage=last_coil_change_milage, last_state_inspection_date=last_state_inspection_date, last_emissions_date=last_emissions_date, last_front_brake_change_milage=last_front_brake_change_milage, last_rear_brake_change_milage=last_rear_brake_change_milage, plate=plate, vin=vin, model=model, notes=notes, active=active, van_count=van_count


# data: [
#           {% for i in van_count %}
#             {
#               van_number: '{{ vans[i] }}',
#               milage: '{{ last_milage[i] }}',
#               last_oil_change_date: '{{ last_oil_change_date[i] }}',
#               last_oil_change_milage: '{{ last_oil_change_milage[i] }}',
#               last_front_tire_change_date: '{{ last_front_tire_change_date[i] }}',
#               last_rear_tire_change_date: '{{ last_rear_tire_change_date[i] }}',
#               last_trans_fluid_change_milage: '{{ last_trans_fluid_change_milage[i] }}',
#               last_battery_change_date: '{{ last_battery_change_date[i] }}',
#               last_air_filter_change_milage: '{{ last_air_filter_change_milage[i] }}',
#               last_spark_plug_change_milage: '{{ last_spark_plug_change_milage[i] }}',
#               last_coil_change_milage: '{{ last_coil_change_milage[i] }}',
#               last_state_inspection_date: '{{ last_state_inspection_date[i] }}',
#               last_emissions_date: '{{ last_emissions_date[i] }}',
#               last_front_brake_change_milage: '{{ last_front_brake_change_milage[i] }}',
#               last_rear_brake_change_milage: '{{ last_rear_brake_change_milage[i] }}',
#               plate: '{{ plate[i] }}',
#               vin: '{{ vin[i] }}',
#               model: '{{ model[i] }}',
#               notes: '{{ notes[i] }}',
#               active: '{{ active[i] }}',
#             },
#           {% endfor %}
#         ],
