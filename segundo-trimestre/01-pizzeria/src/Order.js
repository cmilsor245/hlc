import React from 'react';

export function Order({ openHour, closeHour }) {
  const CURRENT_HOUR = new Date().getHours();
  const IS_OPEN = CURRENT_HOUR >= openHour && CURRENT_HOUR < closeHour;

  return (
    <div className='order'>
      {IS_OPEN ?
        <p>Estamos abiertos desde las {openHour}:00 hasta las {closeHour}:00</p>
        :
        <p>Estamos cerrados</p>}
      <button className='btn'>Order</button>
    </div>
  );
}