<template>
  <section>
    <v-container>
      <v-row justify="center">
        <v-col md="8">
          <v-card elevation="0" class="pa-8">
            <v-card-title>
              Validação {{ label }}
            </v-card-title>
            <v-col>
              <v-row>
                <v-col>
                  <v-text-field
                    v-model="value" 
                    v-mask="mask"
                    :hint="mask"
                    :label="label"
                    :rules="rules"
                    :background-color="inputTextColor"
                    clearable
                    outlined
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-col>
            <v-col>
              <v-row>
                <v-col>
                  <v-btn @click="handleCPF" :class="cpfButtonClass" block> CPF </v-btn>
                </v-col>
                <v-col>
                  <v-btn @click="handleCNPJ" :class="cnpjButtonClass" block> CNPJ </v-btn>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-btn @click="validate" block>Validar</v-btn>
                </v-col>
              </v-row>
            </v-col>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </section>
</template>

<script>
import Vue from 'vue'

import CPFService from '@/services/CPFService.js'
import CNPJService from '@/services/CNPJService.js'


export default Vue.extend({
  computed: {
    cpfButtonClass() {
      return {
        'primary': this.cpfSelected
      }
    },
    cnpjButtonClass() {
      return {
        'primary': !this.cpfSelected
      }
    },
    mask() {
      return this.cpfSelected ? '###.###.###-##' : '##.###.###/####-##'
    },
    rules() {
      return this.cpfSelected ? [] : []
    },
    label() {
      return this.cpfSelected ? 'CPF' : 'CNPJ'
    }
  },
  data() {
    return {
      value: '',
      inputTextColor: '',
      cpfSelected: true,
    }
  },
  methods: {
    validate() {
      const service = this.cpfSelected ? CPFService : CNPJService

      service.validate(this.value)
      .then((response) => {
        if(response.data.valid) {
          this.inputTextColor = 'green accent-4'
        } else {
          this.inputTextColor = 'red accent-4 '
        }
      }).catch((response) => {
        console.log(response)
      })
    },
    handleCPF() {
      this.cpfSelected = true
      this.resetInputTextColor()
    },
    handleCNPJ() {
      this.cpfSelected = false
      this.resetInputTextColor()
    },
    resetInputTextColor() {
      this.inputTextColor = '';
    }
  }
})
</script>