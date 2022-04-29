/*
 * Essa função foi tida como referência a partir do algoritmo disponibilizado pelo site da Receita Federal
 * Link: http://www.receita.fazenda.gov.br/aplicacoes/atcta/cpf/funcoes.js
 */
function cleanCPF(cpf) {
  cpf = cpf.replace('.', '')
  cpf = cpf.replace('.', '')
  cpf = cpf.replace('-', '')

  return cpf
}

function validateCPF(cpf) {
  cpf = cleanCPF(cpf)

  if (knowInvalidCPFs(cpf)) {
    return false;
  }

  return checkFirstDigit(cpf) && checkSecondDigit(cpf)
}

function knowInvalidCPFs(cpf) {
  return [
    "11111111111",
    "22222222222",
    "33333333333",
    "44444444444",
    "55555555555",
    "66666666666",
    "77777777777",
    "88888888888",
    "99999999999",
  ].includes(cpf)
}

function checkFirstDigit(cpf) {
  let sum = 0;
  let remainder;

  const checkDigit1 = parseInt(cpf.substring(9, 10));

  for (let i = 1; i <= 9; i++) {
    sum = sum + parseInt(cpf.substring(i-1, i)) * (11 - i);
  }

  remainder = (sum * 10) % 11;
  if ((remainder == 10) || (remainder == 11)) {
    remainder = 0;
  }

  return remainder == checkDigit1 
}

function checkSecondDigit(cpf) {
  let sum = 0;
  let remainder;

  const checkDigit2 = parseInt(cpf.substring(10, 11));

  for (let i = 1; i <= 10; i++) {
    sum = sum + parseInt(cpf.substring(i-1, i)) * (12 - i);
  }

  remainder = (sum * 10) % 11;

  if ((remainder == 10) || (remainder == 11)) {
    remainder = 0;
  }

  return remainder == checkDigit2
}

export {
  validateCPF
}