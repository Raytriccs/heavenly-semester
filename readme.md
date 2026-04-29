# Heavenly

Heavenly er en enkel nettside for et dessertsted i Strømmen. 
nettsiden hittil er laget med Flask, HTML og CSS, og viser en forside med meny, informasjon om stedet og besøksadresse.

# Innhold

Nettsiden inneholder:
- en navigasjonsmeny
- en hero-seksjon med tittel og beskrivelse
- en meny med noen dessertprodukter
- en "Om oss"-seksjon
- en "Besøk oss"-seksjon
- en footer

# Teknologier brukt

- Python
- Flask
- HTML
- CSS

# Filstruktur

- `app.py` – Flask-applikasjonen
- `app.wsgi` - brukes for kjøring på server 
- `templates/index.html` – HTML-strukturen til nettsiden
- `static/style.css` – design og styling

# Hvordan kjøre prosjektet

1. Sørg for at Python og Flask er installert
2. Kjør prosjektet med:
python3 app.py
3. hvis ikke dette funker, kan du bare skrive ip adressen i nettleseren

# Database

Prosjektet bruker en MySQL-database som heter `heavenly`.

# Hvordan lage databasen

1. Logg inn i MySQL
2. Kjør disse kommandoene:

# For å lage databasen
CREATE DATABASE heavenly;
USE heavenly;

# Lage tabellen menu_items
CREATE TABLE menu_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

# lage tabellen orders
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

# legge inn hele menyen i databasen
INSERT INTO menu_items (name, category, price) VALUES
('Sjokolade Milkshake', 'Milkshakes', 125.00),
('Vanilje Milkshake', 'Milkshakes', 125.00),
('Jordbær Milkshake', 'Milkshakes', 125.00),
('Pistasj Milkshake', 'Milkshakes', 125.00),
('Brownie Milkshake', 'Milkshakes', 129.00),
('Cookie Dough Milkshake', 'Milkshakes', 129.00),
('Salt Karamell Milkshake', 'Milkshakes', 129.00),
('Lotus Biscoff Milkshake', 'Milkshakes', 135.00),
('The Waffle Icon', 'Waffles', 194.00),
('Cookie Heaven', 'Waffles', 199.00),
('Lotus Biscoff Waffle', 'Waffles', 204.00),
('Caramel Dream', 'Waffles', 204.00),
('Waffle Besties', 'Waffles', 209.00),
('Strawberry Joy', 'Waffles', 211.00),
('Fruit Bomb', 'Waffles', 239.00),
('Choco Strawberry', 'Mini Pancakes', 209.00),
('Berrylicious', 'Mini Pancakes', 224.00);

