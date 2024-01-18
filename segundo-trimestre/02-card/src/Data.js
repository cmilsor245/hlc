import React from 'react';
import { SkillList } from './SkillList';
import { Intro } from './Intro';


export function Data() {
  const TITLE_CONTENT = 'CARD 1';
  const PARAGRAPH_CONTENT = 'Sint aliquip proident nostrud do officia. Qui ipsum irure aliqua velit tempor pariatur quis in nisi occaecat. Est id incididunt qui duis reprehenderit proident excepteur eu velit culpa magna. Ad deserunt deserunt culpa anim dolore aliquip. Proident ullamco esse sunt proident consectetur pariatur occaecat sit magna. Sit enim mollit ea ad.';

  return (
    <div className='data'>
      <Intro title={TITLE_CONTENT} description={PARAGRAPH_CONTENT} />
      <SkillList />
    </div>
  );
}
