import React from 'react';
import PropTypes from 'prop-types';
import '../signUpForm.css';
import img from '../icons8-close.svg';

function GetLinkForm ({ link, setForm }) {
  const onCloseHandler = () => {
    setForm();
  };

  return (
    <form className='form'>
      <h2 className='form--title'>Download link</h2>
      <input type='text' value={link}></input>
      <button className='close' onClick={ onCloseHandler }><img src={img} /></button>
    </form>
  );
}

GetLinkForm.propTypes = {
  link: PropTypes.string,
  setForm: PropTypes.func,
};

export default GetLinkForm;
