const validateUsername = (username) => {
  const usernamePattern = /^[a-zA-Z][a-zA-Z0-9]/g;

  if (!usernamePattern.test(username)) {
    return {
      ok: false,
      message: 'Имя пользователя может содержать только латинские буквы и цифры.',
    };
  }

  if (username.length < 4 || username.length > 20) {
    return {
      ok: false,
      message: 'Имя пользователя должно содержать от 4 до 20 символов.',
    };
  }

  return {
    ok: true,
  };
};

const validatePassword = (password) => {
  const numberPattern = /\d/;
  const specialLettersPattern = /[ `!@#$%^&*()_+\-=[\]{};':"\\|,.<>/?~]/;

  if (password.length < 6) {
    return {
      ok: false,
      message: 'Длина пароля должна быть не менее 6 символов.',
    };
  }

  if (password === password.toLowerCase()) {
    return {
      ok: false,
      message: 'Пароль должен содержать заглавную букву',
    };
  }

  if (!numberPattern.test(password)) {
    return {
      ok: false,
      message: 'Пароль должен содержать число',
    };
  }

  if (!specialLettersPattern.test(password)) {
    return {
      ok: false,
      message: 'Пароль должен содержать специальный символ',
    };
  }

  return {
    ok: true,
  };
};

export { validateUsername, validatePassword };
