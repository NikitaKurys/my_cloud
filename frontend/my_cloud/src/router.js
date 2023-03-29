import React from 'react';
import {
  BrowserRouter as Router, Route, Routes,
} from 'react-router-dom';
import StartPage from './components/StartPage/StartPage';
import Header from './components/header/Header';
import SignUpForm from './components/forms/signUpForm/SignUpForm';
import SignInForm from './components/forms/signInForm/SignInForm';
import AdminPanel from './components/admin/AdminPanel';
import Files from './cloud/Files/FileStorage';
import Page404 from './components/Page404/Page404';

function App () {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path='/' element={<StartPage />} />
        <Route path='/sign-up' element={<SignUpForm />} />
        <Route path='/sign-in' element={<SignInForm />} />
        <Route path='/admin' element={<AdminPanel />} />
        <Route path='/cloud' element={<Files />} />
        <Route path='*' element={<Page404 />} />
      </Routes>
    </Router>
  );
}

export default App;
