import React, {
  useContext, useEffect, useRef, useState,
} from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Cookies from 'js-cookie';
import Preloader from '../Preloader/Preloader';
import { logIn } from '../../api/requests';
import Context from '../../GlobalState/state';
import '../formStyle/Form.css';
import img from '../formStyle/icons8-close.svg';

function SignInForm() {
  const username = useRef();
  const password = useRef();
  const [sendRequest, setSendRequest] = useState(false);
  const [error, setError] = useState();
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();

  const { setSessionId } = useContext(Context);

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);

      const response = await logIn(username.current.value, password.current.value);
      const data = await response.json();

      if (!response.ok) {
        setError(Object.values(data));
        setSendRequest(false);
        setIsLoading(false);
        return;
      }

      setSessionId(Cookies.get('sessionid'));

      navigate('/my-cloud/');

      setSendRequest(false);
      setIsLoading(false);
    };

    if (sendRequest) {
      fetchData();
    }
  }, [sendRequest]);

  const onSubmitHandler = (e) => {
    e.preventDefault();
    setSendRequest(true);
  };

  return (
    <>
      <form className="form" onSubmit={onSubmitHandler}>
        <h2 className="form--title">Вход</h2>
        <input type="username" ref={username} placeholder="псевдоним" required />
        <input type="password" ref={password} placeholder="пароль" required />
        <input type="submit" value="OK" required />
        <span>{error}</span>
        <button className="close" type="button" aria-label="Close"><Link to="/"><img src={img} alt="close" /></Link></button>
      </form>
      { isLoading ? <Preloader /> : null }
    </>
  );
}

export default SignInForm;
