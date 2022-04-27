import _axios from '@/services';

export default {
  validate: (cpf) => _axios.get('validate', { params: cpf }),
};
