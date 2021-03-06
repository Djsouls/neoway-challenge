import axios from 'axios';

const config = {
  baseURL: process.env.VUE_APP_API_BASE_URL,
  headers: {
    Accept: 'application/json'
  }
};

const _axios = axios.create(config);

export default _axios;