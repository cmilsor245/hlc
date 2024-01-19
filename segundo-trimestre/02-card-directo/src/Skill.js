import React from 'react';


export function Skill({objeto_skill}) {
  let level;
  if (objeto_skill.level === 'beginner') {
    level = '😪';
  } else if (objeto_skill.level === 'intermediate') {
    level = '😀';
  } else {
    level = '😎';
  }

  return (
    <div className='skill' style={{ backgroundColor: objeto_skill.color }}>
      <span>{objeto_skill.skill}</span>
      <span>{level}</span>
    </div>
  );
}
