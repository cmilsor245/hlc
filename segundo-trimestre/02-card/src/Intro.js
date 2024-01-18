import React from 'react';


export function Intro(props) {
  return (
    <>
      <h1>{props.title}</h1>
      <p>{props.description}</p>
    </>
  );
}
