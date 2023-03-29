const storage = window.localStorage;

export const addDataToStorage = (data) => {
  storage.setItem('token', JSON.stringify(data.token));
  storage.setItem('username', JSON.stringify(data.username));
};

export const getDataFromStorage = () => {
  return {
    token: JSON.parse(storage.getItem('token')),
    username: JSON.parse(storage.getItem('username')),
  };
};

export const removeDataFromStorage = () => {
  storage.clear();
};
