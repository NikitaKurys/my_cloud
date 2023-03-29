import React from 'react';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import Username from './Username';
import './header.css';

function Header () {
  const isAuth = useSelector(state => state.auth.authToken);
  const username = useSelector(state => state.auth.username);

  return (
    <section className="header">
      <div className='header--logo'><Link to='/'>My_Cloud</Link></div>
      <div className='header--menu-container'>{
        !isAuth
          ? <>
              <div className='header--menu-container--item'><Link to='/sign-in'>Войти</Link></div>
              <div className='header--menu-container--item'><Link to='/sign-up'>Регистрация</Link></div>
            </>
          : <Username username={ username } />
      }</div>
    </section>
  );
}

export default Header;
