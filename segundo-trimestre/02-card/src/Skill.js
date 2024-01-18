import React from 'react';


export function Skill(props) {
  let level = '';
  if (props.objeto_skill.level === 'beginner') {
    level = '😪';
  } else if (props.objeto_skill.level === 'intermediate') {
    level = '😀';
  } else {
    level = '😎';
  }

  return (
    <div className='skill' style={{ backgroundColor: props.objeto_skill.color }}>
      <span>{props.objeto_skill.skill}</span>
      <span>{level}</span>
    </div>
  );
}
