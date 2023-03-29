import React, { useEffect, useRef } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import PropTypes from 'prop-types';
import '../signUpForm.css';
import img from '../icons8-close.svg';
import { patchFile } from '../../../api/requests';

function FileRenameForm ({ token }) {
  const location = useLocation();
  const navigate = useNavigate();
  const newFileName = useRef();

  useEffect(() => {
    newFileName.current.value = location.state.file_name;
  }, []);

  const onSubmitHandler = async (e) => {
    e.preventDefault();

    const data = location.state;
    data.file_name = newFileName.current.value;

    const response = await patchFile(token, data);

    if (response.ok) {
      navigate('/cloud/');
    }
  }

  return (
    <form className='form' onSubmit={ onSubmitHandler }>
      <h2 className='form-title'>Rename file</h2>
      <input type='text' placeholder='new name' ref={ newFileName }></input>
      <input type='submit' value='OK' required></input>
      <button className='close'><Link to='/cloud/'><img src={img} /></Link></button>
    </form>
  )
}

FileRenameForm.propTypes = {
  token: PropTypes.string;
}

export default FileRenameForm;
