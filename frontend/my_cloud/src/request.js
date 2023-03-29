import useSWR from 'swr';

const fetcher = async ([url, method, body, token]) => {
  try {
    const response = await fetch(url, {
      method,
      headers: {
        'Content-Type': 'application/json',
        Authorization: token ? `Token ${token}` : null,
      },
      body: body ? JSON.stringify(body) : null
    })
    const json = await response.json();
    json.ok = response.ok;
    return json;
  } catch (error) {
    return error;
  }
}

const useRequest = (args) => {
  const { data, error, isLoading } = useSWR(!args ? null : [...args], fetcher)

  return {
    data,
    error,
    isLoading,
  }
};

export default useRequest;
