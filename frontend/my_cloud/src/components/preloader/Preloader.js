import React from 'react';
import preloader from './preloader.gif';
import './Preloader.css';

function Preloader () {
  return (
    <img className='preloader' src={ preloader }></img>
  );
}

export default Preloader;
