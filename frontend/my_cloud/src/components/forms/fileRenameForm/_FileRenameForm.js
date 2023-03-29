import React, { useEffect, useRef } from 'react';
import { useSelector } from 'react-redux';
import PropTypes from 'prop-types';
import '../signUpForm.css';
import img from '../icons8-close.svg';
import { patchFile } from '../../../api/requests';

function FileRenameForm ({ currentFile, setForm, setFiles }) {
  const token = useSelector(state => state.auth.authToken);
  const newFileName = useRef();

  useEffect(() => {
    newFileName.current.value = currentFile.file_name;
  }, []);

  const onSubmitHandler = async (e) => {
    e.preventDefault();

    const patchData = currentFile;
    patchData.file_name = newFileName.current.value;

    const response = await patchFile(token, patchData);
    const data = await response.json();

    if (response.ok) {
      setFiles(data);
      setForm();
    }
  };

  const onCloseHandler = () => {
    setForm();
  };

  return (
    <form className='form' onSubmit={ onSubmitHandler }>
      <h2 className='form-title'>Rename file</h2>
      <input type='text'placeholder='new name' ref={ newFileName }></input>
      <input type='submit' value='OK' required></input>
      <button className='close' onClick={ onCloseHandler }><img src={img} /></button>
    </form>
  );
}

FileRenameForm.propTypes = {
  currentFile: PropTypes.object,
  setForm: PropTypes.func,
  setFiles: PropTypes.func,
};

export default FileRenameForm;
