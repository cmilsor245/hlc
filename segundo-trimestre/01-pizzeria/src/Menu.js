import React from 'react';
import { PIZZA_DATA } from '.';
import { Pizza } from './Pizza';

export function Menu() {
  return (
    <main className='menu'>
      <h2>Nuestro menú</h2>
      <p>Do veniam magna enim occaecat. Labore eu cupidatat magna aute officia esse laborum excepteur do deserunt labore nostrud dolore tempor. Ad Lorem culpa est qui velit sunt ad elit sunt consequat adipisicing dolor. Officia minim laboris occaecat excepteur in excepteur eu aliquip sit dolore cupidatat. Velit proident magna est commodo. Id id enim consequat id adipisicing magna dolore voluptate ullamco do Lorem ad.Lorem excepteur ex deserunt velit nostrud fugiat ullamco duis irure. Aliqua commodo velit ipsum proident ex sunt reprehenderit laborum proident elit sit ad amet. Sint amet culpa Lorem enim nulla Lorem sit do est ex. Officia sit culpa nostrud dolor culpa in ut sunt.</p>
      {/* utilizo operadores lógicos */}
      {/* {PIZZA_DATA.length > 0 &&
              <ul className = 'pizzas'>
                {PIZZA_DATA.map((itemPizza) => <Pizza
                  objetoPizza = {itemPizza}
                />)}
              </ul>
            } */}

      {PIZZA_DATA.length > 0 ?
        <ul className='pizzas'>
          {PIZZA_DATA.map((itemPizza) => <Pizza
            objetoPizza={itemPizza}
            key={itemPizza.name} />)}
        </ul>
        :
        <p>No hay pizzas disponibles</p>}
    </main>
  );
}