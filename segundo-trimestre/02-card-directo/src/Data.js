import React from 'react';
import { SkillList } from './SkillList';
import { Intro } from './Intro';


export function Data() {
  const TITLE = 'CARD 1';
  const DESCRIPTION = 'Ullamco non id voluptate ut ad ea in laboris ad. Reprehenderit qui velit occaecat aliqua nisi deserunt cillum deserunt consectetur laborum ut est dolor laboris. Dolore do proident laborum eiusmod duis minim adipisicing et elit. Enim proident magna aute commodo pariatur dolor amet qui magna.';

  return (
    <div className='data'>
      <Intro title={TITLE} description={DESCRIPTION} />
      <SkillList />
    </div>
  );
}
