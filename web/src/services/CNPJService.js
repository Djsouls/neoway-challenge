import _axios from '@/services';

export default {
  index: () => _axios.get('/'),
  all: () => _axios.get('/cnpjs'),
  create: (cnpj) => _axios.post('/cnpj', { cnpj: cnpj }),
  delete: (id) => _axios.delete(`/cnpj/${id}`),
  validate: (cnpj) => _axios.get('cnpj/validate', { params: { cnpj: cnpj }}),
  block: (id) => _axios.put(`/cnpj/${id}/block`)
};
