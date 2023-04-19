import React, { useContext } from 'react';
import PropTypes from 'prop-types';
import { useNavigate } from 'react-router-dom';
import Context from '../../GlobalState/state';

function UserStorage({ storageUserId }) {
  const { setCurrentStorageUser } = useContext(Context);
  const navigate = useNavigate();

  const onClickHandler = () => {
    setCurrentStorageUser();
    navigate('/admin');
  };

  return (
    <div className="storage-user">
      <span
        className="storage-user-id"
      >
        {`Хранилище пользователя с ID ${storageUserId}`}
      </span>
      <button
        className="storage-user--exit-btn"
        type="button"
        onClick={onClickHandler}
      >
        Покинуть хранилище
      </button>
    </div>
  );
}

UserStorage.propTypes = {
  storageUserId: PropTypes.number.isRequired,
};

export default UserStorage;
