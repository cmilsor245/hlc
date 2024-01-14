import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

const pizzaData = [
  {
    name: 'Focaccia',
    ingredients: 'Bread with italian olive oil and rosemary',
    price: 6,
    photoName: 'pizzas/focaccia.jpg',
    soldOut: false,
  },
  {
    name: 'Pizza Margherita',
    ingredients: 'Tomato and mozarella',
    price: 10,
    photoName: 'pizzas/margherita.jpg',
    soldOut: false,
  },
  {
    name: 'Pizza Spinaci',
    ingredients: 'Tomato, mozarella, spinach, and ricotta cheese',
    price: 12,
    photoName: 'pizzas/spinaci.jpg',
    soldOut: false,
  },
  {
    name: 'Pizza Funghi',
    ingredients: 'Tomato, mozarella, mushrooms, and onion',
    price: 12,
    photoName: 'pizzas/funghi.jpg',
    soldOut: false,
  },
  {
    name: 'Pizza Salamino',
    ingredients: 'Tomato, mozarella, and pepperoni',
    price: 15,
    photoName: 'pizzas/salamino.jpg',
    soldOut: true,
  },
  {
    name: 'Pizza Prosciutto',
    ingredients: 'Tomato, mozarella, ham, aragula, and burrata cheese',
    price: 18,
    photoName: 'pizzas/prosciutto.jpg',
    soldOut: false,
  },
];

function App() {
  return (
    <div>
      <Header />
      <Menú />
      <Footer />
    </div>
  );
}

function Header() {
  /* const STYLE = {
    color : 'red',
    textAlign: 'center',
    textTransform: 'uppercase'
  } */
  return (
    <header className = 'header'>
      <h1 /* style = {STYLE} */>
        pizzería torre del mar
      </h1>
    </header>
  );
}

function Menú() {
  return (
    <main className = 'menu'>
      <h2>Nuestro menú</h2>
      <p>Do veniam magna enim occaecat. Labore eu cupidatat magna aute officia esse laborum excepteur do deserunt labore nostrud dolore tempor. Ad Lorem culpa est qui velit sunt ad elit sunt consequat adipisicing dolor. Officia minim laboris occaecat excepteur in excepteur eu aliquip sit dolore cupidatat. Velit proident magna est commodo. Id id enim consequat id adipisicing magna dolore voluptate ullamco do Lorem ad.Lorem excepteur ex deserunt velit nostrud fugiat ullamco duis irure. Aliqua commodo velit ipsum proident ex sunt reprehenderit laborum proident elit sit ad amet. Sint amet culpa Lorem enim nulla Lorem sit do est ex. Officia sit culpa nostrud dolor culpa in ut sunt.</p>
      {/* {pizzaData.length > 0 && // utilizo operadores lógicos
        <ul className = 'pizzas'>
          {pizzaData.map((itemPizza) => <Pizza
            objetoPizza = {itemPizza}
          />)}
        </ul>
      } */}

      {pizzaData.length > 0 ?
        <ul className = 'pizzas'>
          {pizzaData.map((itemPizza) => <Pizza
            objetoPizza = {itemPizza}
          />)}
        </ul>
      :
        <p>No hay pizzas disponibles</p>
      }
    </main>
  );
}

function Pizza(props) {
  return (
    <li className = 'pizza'>
      <img src = {props.objetoPizza.photoName} alt = {props.objetoPizza.name} />
      <h3>{props.objetoPizza.name}</h3>
      <p>{props.objetoPizza.ingredients}</p>
      <p>{props.objetoPizza.price}</p>
    </li>
  );
}

function Footer() {
  const CURRENT_HOUR = new Date().getHours();
  const OPEN_HOUR = 8;
  const CLOSE_HOUR = 23;
  const IS_OPEN = CURRENT_HOUR >= OPEN_HOUR && CURRENT_HOUR < CLOSE_HOUR;

  return (
    <footer className = 'footer'>
      <div className = 'order'>
        {IS_OPEN ? 
          <p>Estamos abiertos desde las {OPEN_HOUR}:00 hasta las {CLOSE_HOUR}:00</p>
        :
          <p>Estamos cerrados</p>
        }
        <button className = 'btn'>Order</button>
      </div>
    </footer>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);