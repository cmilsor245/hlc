import React, { useState } from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'

function App() {
  const [STEP, setStep] = useState(1)
  const [IS_OPEN, setIsOpen] = useState(true)

  function handlePrevious() {
    if (STEP > 1) setStep(STEP - 1)
  }

  function handleNext() {
    if (STEP < 3) setStep(STEP + 1)
  }

  function handleOpen() {
    setIsOpen(!IS_OPEN)
  }

  const DATA = [
    'aprende react😎',
    'aprende javascript🤪',
    'aprende css😏'
  ]

  return (
    <>
      <button className = 'close' onClick = {handleOpen}>
        &times;
      </button>
      {IS_OPEN && (
        <>
          {/* <div className = {IS_OPEN ? 'steps' : 'ocultar'} */}
          <div className = 'steps'>
            <div className = 'numbers'>
              <div className = {`${STEP >= 1 ? 'active' : ''}`}>1</div>
              <div className = {`${STEP >= 2 ? 'active' : ''}`}>2</div>
              <div className = {`${STEP >= 3 ? 'active' : ''}`}>3</div>
            </div>
            <p className = 'message'>{DATA[STEP - 1]}</p>
            <div className = 'buttons'>
              <Button
                style = {{ backgroundColor: '#7950f2', color: '#fff' }}
                onClick = {handlePrevious}
                text = 'previous'
                emoji = '🤪'
              />
              <Button
                style = {{ backgroundColor: '#7950f2', color: '#fff' }}
                onClick = {handleNext}
                text = 'next'
                emoji = '😎'
              />
            </div>
          </div>
        </>
      )}
    </>
  )
}

function Button({ style, onClick, text, emoji }) {
  return (
    <button style = {style} onClick = {onClick}>
      {emoji} {text}
    </button>
  )
}

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)