import React, { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import FileInput from './FileInput';
import FileList from './FileList';
import FileEditPanel from './FileEditPanel';
import { postFile, getFiles } from '../../api/requests';

function FileStorage () {
  const token = useSelector(state => state.auth.authToken);
  const [currentFile, setCurrentFile] = useState();
  const [files, setFiles] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await getFiles(token);
      const data = await response.json();

      setFiles(data);
    };

    fetchData();
  }, []);

  const sendFile = async (file) => {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('comment', '');
    const response = await postFile(token, formData);
    const data = await response.json();

    setFiles(data);
  };

  return (
    <>
    <FileList
      fileList={ files }
      setCurrentFile={ setCurrentFile }
      currentFile={ currentFile }
      />
    <FileInput sendFile={ sendFile } />
    { currentFile
      ? <FileEditPanel currentFile={ currentFile } setFiles={ setFiles } setCurrentFile={ setCurrentFile } />
      : null }
    </>
  );
}

export default FileStorage;
