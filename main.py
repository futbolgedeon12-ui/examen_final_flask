from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        edad = int(request.form.get("edad", 0))
        cantidad = int(request.form.get("cantidad", 0))

        precio_tarro = 9000
        total_sin_descuento = cantidad * precio_tarro

        if 18 <= edad <= 30:
            porcentaje_descuento = 0.15
        elif edad > 30:
            porcentaje_descuento = 0.25
        else:
            porcentaje_descuento = 0.0

        descuento = total_sin_descuento * porcentaje_descuento
        total_a_pagar = total_sin_descuento - descuento

        resultado = {
            "nombre": nombre,
            "total_sin_descuento": total_sin_descuento,
            "descuento": descuento,
            "total_a_pagar": total_a_pagar,
        }

    return render_template("ejercicio1.html", resultado=resultado)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None
    usuarios = {
        "juan": ("admin", "Bienvenido Administrador juan"),
        "pepe": ("user", "Bienvenido Usuario pepe"),
    }

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        contrasena = request.form.get("contrasena", "")

        if nombre in usuarios and usuarios[nombre][0] == contrasena:
            mensaje = usuarios[nombre][1]
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)