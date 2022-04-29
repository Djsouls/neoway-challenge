import _axios from '@/services';

export default {
  index: () => _axios.get('/'),
  all: () => _axios.get('/cpfs'),
  create: (cpf) => _axios.post('/cpf', { cpf: cpf }),
  delete: (id) => _axios.delete(`/cpf/${id}`),
  validate: (cpf) => _axios.get('cpf/validate', { params: { cpf: cpf }}),
  block: (id) => _axios.put(`/cpf/${id}/block`)
};
