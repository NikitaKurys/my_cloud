import BASE_URL from '../config'

export function logIn (username, password) {
  return fetch(BASE_URL + 'api/v1/cloud/auth/token/login/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      username,
      password
    }),
  });
}

export function logOut (token) {
  return fetch(BASE_URL + 'api/v1/cloud/auth/token/logout/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Token ${token}`
    },
  });
}

export function userMe (token) {
  return fetch(BASE_URL + 'api/v1/cloud/auth/users/me/', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Token ${token}`
    },
  });
}

export function getUserList (token) {
  return fetch(BASE_URL + 'api/v1/cloud/detail_users_list/', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Token ${token}`
    },
  });
}

export function deleteUser (token, password, id) {
  return fetch(BASE_URL + `auth/users/${id}/`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Token ${token}`
    },
    body: JSON.stringify({
      current_password: password
    }),
  });
}

export function patchUser (token, id, isStaff) {
  return fetch(BASE_URL + `auth/users/${id}/`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Token ${token}`
    },
    body: JSON.stringify({
      is_staff: isStaff
    }),
  });
}

export function signUp (data) {
  return fetch(BASE_URL + 'api/v1/cloud/registr/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
}

export function postFile (token, data) {
  return fetch(BASE_URL + 'api/v1/cloud/files/', {
    method: 'POST',
    headers: {
      Authorization: `Token ${token}`
    },
    body: data
  });
}

export function getFiles (token) {
  return fetch(BASE_URL + 'api/v1/cloud/files/', {
    method: 'GET',
    headers: {
      Authorization: `Token ${token}`
    },
  });
}

export function patchFile (token, data) {
  return fetch(BASE_URL + 'api/v1/cloud/files/', {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Token ${token}`
    },
    body: JSON.stringify(data)
  });
}

export function deleteFile (token, id) {
  return fetch(BASE_URL + `api/v1/cloud/files/?id=${id}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Token ${token}`
    },
  });
}

export function downloadFile (token, id) {
  return fetch(BASE_URL + `api/v1/cloud/link/${id}/`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Token ${token}`
    },
  });
}

export function getDownloadLink (token, id) {
  return fetch(BASE_URL + `api/v1/cloud/link/?file_id=${id}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Token ${token}`
    },
  });
}

export function getProfile (token) {
  return fetch(BASE_URL + 'api/v1/cloud/profile/', {
    method: 'GET',
    headers: {
      Authorization: `Token ${token}`
    },
  });
}
