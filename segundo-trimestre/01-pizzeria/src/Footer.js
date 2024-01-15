import React from 'react';
import { Order } from './Order';

export function Footer() {
  const OPEN_HOUR = 8;
  const CLOSE_HOUR = 18;

  // utilizo if else
  /* if (IS_OPEN) {
    return (
      <footer className = 'footer'>
        <div className = 'order'>
          <p>Estamos abiertos desde las {OPEN_HOUR}:00 hasta las {CLOSE_HOUR}:00</p>
          <button className = 'btn'>Order</button>
        </div>
      </footer>
    )
  } else {
    return (
      <footer className = 'footer'>
        <div className = 'order'>
          <p>Estamos cerrados</p>
          <button className = 'btn'>Order</button>
        </div>
      </footer>
    )
  } */
  return (
    <footer className='footer'>
      <Order openHour={OPEN_HOUR} closeHour={CLOSE_HOUR} />
    </footer>
  );
}