import React, { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import { userMe } from '../../api/requests';
import UsersList from './UsersList';
import './AdminPanel.css';
import Preloader from '../preloader/Preloader';

function AdminPanel () {
  const token = useSelector(state => state.auth.authToken);
  const [access, setAccess] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);
      const response = await userMe(token);
      const data = await response.json();

      if (data.is_staff) {
        setAccess(true);
      }

      setIsLoading(false);
    };

    fetchData();
  }, []);

  return (
    isLoading
      ? <Preloader />
      : !access
          ? <div className='admin-panel--access-denied'>
              <span className='content'>{'Упс, что-то пошло не так'}</span>
            </div>
          : <UsersList />
  );
};

export default AdminPanel;
