import PropTypes from 'prop-types';
import React, { useRef, useState } from 'react';
import './FileInput.css';

function FileInput ({ sendFile }) {
  const file = useRef();
  const [fileChosen, setFileChosen] = useState();

  const onChangeHandler = () => {
    setFileChosen(file.current.files);
  };

  const onSubmitHandler = (e) => {
    e.preventDefault();
    setFileChosen();
    sendFile(fileChosen.item(0));
  };

  return (
    <form className='file-input-form' onSubmit={onSubmitHandler}>
      <div className='input-wrapper button'>
        <input type='file' id='input_file' ref={file} onChange={onChangeHandler}></input>
        <label htmlFor='input_file'>
          <span>Загрузить файл</span>
        </label>
        { fileChosen && fileChosen.length
          ? <span className='preview'>{ fileChosen.item(0).name }</span>
          : null }
        </div>
        { fileChosen && fileChosen.length
          ? <input type={'submit'} value={'Отправить'}/>
          : null }
    </form>
  );
}

FileInput.propTypes = {
  sendFile: PropTypes.func,
};

export default FileInput;
