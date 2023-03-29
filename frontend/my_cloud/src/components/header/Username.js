import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { logout } from '../../reduxStore/auth/authSlice';
import { logOut, userMe } from '../../api/requests';

function Username ({ username }) {
  const [logoutButton, setLogoutButton] = useState(false);
  const [sendRequest, setSendRequest] = useState(false);
  const [user, setUsername] = useState(username);
  const token = useSelector(state => state.auth.authToken);
  const dispatch = useDispatch();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      const response = await userMe(token);
      const data = await response.json();

      setUsername(data.username);
    };

    if (token) {
      fetchData();
    }
  }, []);
  useEffect(() => {
    const fetchData = async () => {
      const response = await logOut(token);

      if (response.ok) {
        dispatch(logout());

        navigate('/');
      }
    };

    if (sendRequest) {
      fetchData();
      setSendRequest(false);
    }
  }, [sendRequest]);

  const onMouseEnterHandler = () => {
    setLogoutButton(true);
  };

  const onMouseLeaveHandler = () => {
    setLogoutButton(false);
  };

  const onClickHandler = () => {
    setSendRequest(true);
  };

  return (
    logoutButton
      ? <div
      className='header--logout-btn'
      onMouseLeave={onMouseLeaveHandler}
      onClick={onClickHandler}
      >{'Выйти'}</div>
      : <div
      className='header--logout-btn'
      onMouseEnter={onMouseEnterHandler}
      onMouseLeave={onMouseLeaveHandler}
      >{ user }</div>
  );
}

Username.propTypes = {
  username: PropTypes.string,
};

export default Username;
