import { createSlice } from '@reduxjs/toolkit';
import { getDataFromStorage, addDataToStorage, removeDataFromStorage } from '../../cloud/localCloud/cloud';

const authSlice = createSlice(
  {
    name: 'authSlice',
    initialState: {
      authToken: getDataFromStorage().token ? getDataFromStorage().token : null,
      username: getDataFromStorage().username ? getDataFromStorage().username : null,
    },
    reducers: {
      login (state, action) {
        state.authToken = action.payload.token;

        addDataToStorage({
          token: state.authToken,
          username: state.username,
        });
      },
      logout (state) {
        state.authToken = null;
        state.username = null;

        removeDataFromStorage();
      },
    },
  },
);

export const { login, logout, getFromCookie } = authSlice.actions;
export default authSlice.reducer;
