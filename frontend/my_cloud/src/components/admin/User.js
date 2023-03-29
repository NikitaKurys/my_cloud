import React, { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import PropTypes from 'prop-types';
import IsStaffBtn from './IsStaffButton';
import { deleteUser, patchUser } from '../../api/requests';
import img from '../forms/icons8-close.svg';
import './AdminPanel.css';

function User ({ id, username, firstName, lastName, email, numOfFiles, size, isStaff, removeItem }) {
  const [sendRequest, setSendRequest] = useState('');
  const [currentPassword, setCurrentPassword] = useState('');
  const [_isStaff, _setIsStaff] = useState(isStaff);
  const token = useSelector(state => state.auth.authToken);

  useEffect(() => {
    const fetchDataDelete = async () => {
      const response = await deleteUser(token, currentPassword, id);

      if (response.ok) {
        removeItem(id);
      }
    };

    const fetchDataPatch = async () => {
      await patchUser(token, id, _isStaff);
    };

    if (sendRequest === 'DELETE') {
      fetchDataDelete();
      setSendRequest('');
    }

    if (sendRequest === 'PATCH') {
      fetchDataPatch();
      setSendRequest('');
    }
  }, [sendRequest]);

  const onClickHandler = (method) => {
    if (method === 'DELETE') {
      const currentPassword = prompt('Введите Ваш пароль');
      setCurrentPassword(currentPassword);
    }
    setSendRequest(method);
  };

  return (
    <tr key={ id }>
      <td>{ username }</td>
      <td>{ firstName }</td>
      <td>{ lastName }</td>
      <td>{ email }</td>
      <td>{ numOfFiles }</td>
      <td>{ size }</td>
      <td><IsStaffBtn isStaff={ _isStaff } setIsStaff={ _setIsStaff} onClickHandler={onClickHandler} /></td>
      <td><img src={img} onClick={() => onClickHandler('DELETE')}></img></td>
    </tr>
  );
}

User.propTypes = {
  id: PropTypes.number,
  username: PropTypes.string,
  firstName: PropTypes.string,
  lastName: PropTypes.string,
  email: PropTypes.string,
  numOfFiles: PropTypes.number,
  size: PropTypes.number,
  isStaff: PropTypes.bool,
  removeItem: PropTypes.func,
};

export default User;
