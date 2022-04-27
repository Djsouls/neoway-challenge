<template>
  <section>
    <v-container>
      <v-row justify="center">
        <v-col md="6">
          <v-card elevation="0" class="pa-8">
            <v-card-title>
              Valide esta _  
            </v-card-title>
            <v-col>
              <v-row>
                <v-col>
                  <v-text-field
                    v-model="value" 
                    label="Documento"
                    clearable
                    v-mask="mask"
                    :hint="mask"
                    outlined
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-col>
            <v-col>
              <v-row>
                <v-col>
                  <v-btn @click="handleCPF" :color="toggle ? 'primary' : 'disabled'" block> CPF </v-btn>
                  <v-btn @click="toggle = !toggle" :color="toggle ? 'primary' : 'disabled'" block> CPF </v-btn>
                </v-col>
                <v-col>
                  <v-btn @click="toggle = !toggle" :color="!toggle ? 'primary' : 'disabled'" block> CNPJ </v-btn>
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

import CPFValidateService from '@/services/CPFValidateService.js'

export default Vue.extend({
  data() {
    return {
      value: '',
      toggle: true,
    }
  },
  computed: {
    mask() {
      return this.toggle ? '###.###.###-##' : '##.###.###/####-##'
    },
    rules() {
      return this.toggle ? [] : []
    },
    label() {
      return this.toggle ? 'CPF' : 'CNPJ'
    }
  },
  methods: {
    async testService() {
      CPFValidateService.validate()
      .then((r) => {
        console.log(r);
      }).catch((r) => {
        console.log(r);
      });
    },
    handleCPF() {
      this.testService();
    }
  }
})
</script>