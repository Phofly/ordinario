from flask import Flask, render_template, request, redirect
import csv
from datetime import datetime

app = Flask(_name_)

@app.route("/ordinario", methods=["GET", "POST"])
def ordinario():
    if request.method == "POST":
        fecha = datetime.today().strftime('%Y-%m-%d')
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        pin = request.form["pin"]
        medio = request.form["medio"]
        equipo = request.form["equipo"]
        reparacion = request.form["reparacion"]
        estatus = request.form["estatus"]

        with open("prospectos.csv", mode="a", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([fecha, nombre, correo, telefono, pin, medio, equipo, reparacion, estatus])

        return redirect("/ordinario")
return render_template("formulario.html")