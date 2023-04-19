import React, { useContext, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Context from '../../GlobalState/state';
import './StartPage.css';
import img from './my_cloud.svg';

function StartPage() {
  const navigate = useNavigate();
  const { sessionId } = useContext(Context);

  const onClickHandler = () => {
    navigate('/sign-up/');
  };

  useEffect(() => {
    if (sessionId) {
      navigate('/my-cloud/');
    }
  }, [sessionId]);

  return (
    !sessionId
      ? (
        <section className="start-page">
          <div className='start-page--welcome'>
            <h1 className='start-page--welcome--title'>Скачивайте,храните, загружайте ваши файлы.</h1>
            <h2 className='start-page--welcome--subtitle'>Зарегистрируйтесь, чтоб опробовать приложение.</h2>
          </div>
          <img className='start-page--image' src={img} />
        </section>
      )
      : null
  );
}

export default StartPage;
