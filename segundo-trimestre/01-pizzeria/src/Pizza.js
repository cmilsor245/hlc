import React from 'react';

export function Pizza(props) {
  return (
    <li className={`pizza ${props.objetoPizza.soldOut ? 'sold-out' : ''}`}> {/* condiciones para agregar una clase u otra */}
      <img src={props.objetoPizza.photoName} alt={props.objetoPizza.name} />
      <h3>{props.objetoPizza.name}</h3>
      <p>{props.objetoPizza.ingredients}</p>
      <p>{props.objetoPizza.price}</p>
    </li>
  );
}