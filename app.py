from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

# Rodzaje betonu
rodzaje_betonu = {
    1: "Beton C12/15",
    2: "Beton C16/20",
    3: "Beton C25/30",
    4: "Beton C30/37",
    5: "Beton C40/50",
}


# Funkcja do obliczania terminu transportu
def oblicz_termin_transportu(ilosc):
    # Pojemności samochodów
    pojazdy = [3.5, 3.5, 6]  # dwa 3.5m3 i jeden 6m3
    laczna_pojemnosc = sum(pojazdy)
    transporty = ilosc / laczna_pojemnosc
    return round(transporty)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        wybor = int(request.form.get('beton'))
        ilosc = float(request.form.get('ilosc'))

        # Obliczanie transportu i terminów
        transporty = oblicz_termin_transportu(ilosc)
        termin_produkcji = datetime.now() + timedelta(days=1)
        termin_transportu = termin_produkcji + timedelta(days=1)

        # Wyniki przekazujemy do szablonu
        return render_template('result.html',
                               beton=rodzaje_betonu[wybor],
                               ilosc=ilosc,
                               transporty=transporty,
                               termin_produkcji=termin_produkcji,
                               termin_transportu=termin_transportu)

    return render_template('index.html', rodzaje_betonu=rodzaje_betonu)


if __name__ == '__main__':
    app.run(debug=True)
