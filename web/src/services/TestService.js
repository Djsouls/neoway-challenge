import _axios from '@/services';

export default {
  index: () => _axios.get('/'),
};
