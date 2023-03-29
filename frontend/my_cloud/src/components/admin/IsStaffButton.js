import React from 'react';
import PropTypes from 'prop-types';
import './AdminPanel.css';

function IsStaffBtn ({ isStaff, onClickHandler, setIsStaff }) {
  const _onClickHandler = () => {
    setIsStaff(!isStaff);
    onClickHandler('PATCH');
  };

  return (
    <div className={`is-staff-btn-container ${isStaff ? 'on' : 'off'}`} onClick={_onClickHandler} >
      <div className={'is-staff-btn'} ></div>
    </div>
  );
}

IsStaffBtn.propTypes = {
  isStaff: PropTypes.bool,
  onClickHandler: PropTypes.func,
  setIsStaff: PropTypes.func,
};

export default IsStaffBtn;
