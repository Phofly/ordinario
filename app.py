from flask import Flask, render_template, request, redirect
import csv
from datetime import datetime

app = Flask(__name__)

# Ruta raíz redirige al formulario
@app.route("/")
def inicio():
    return redirect("/ordinario")

@app.route("/ordinario", methods=["GET", "POST"])
def ordinario():
    if request.method == "POST":
        fecha = datetime.today().strftime('%Y-%m-%d')
        datos = {
            "nombre": request.form["nombre"],
            "correo": request.form["correo"],
            "telefono": request.form["telefono"],
            "pin": request.form["pin"],
            "medio": request.form["medio"],
            "equipo": request.form["equipo"],
            "reparacion": request.form["reparacion"],
            "estatus": request.form["estatus"]
        }

        with open("prospectos.csv", "a", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([fecha] + list(datos.values()))

        return redirect("/ordinario")
    else:
        fecha = datetime.today().strftime('%Y-%m-%d')
        return render_template("formulario.html", fecha=fecha)

if __name__ == "__main__":
    app.run(debug=True)

