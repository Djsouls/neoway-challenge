<template>
  <section class="py-8">
    <v-dialog
      v-model="addDialog"
      max-width="500px"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          v-on="on"
          color="secondary"
          fab
          fixed
          top
          right
        >
          <v-icon>mdi-plus</v-icon>
        </v-btn>
      </template>
      <v-card>
        <v-card-title>Adicionar {{ select }}</v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-text-field
                v-model="itemToBeAdded"
                v-mask="mask"
                :label="select"
                :rules="[rules.validate]"
              ></v-text-field>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            @click="closeAddDialog"
          >Fechar</v-btn>
          <v-btn
            @click="addItem"
          >Salvar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-row justify="center">
      <v-col cols="8">
        <v-text-field
          v-model="searchText"
          append-icon="mdi-magnify"
          label="Pesquise"
        >
        </v-text-field>
      </v-col>
      <v-col cols="2">
        <v-select
          cols="4"
          v-model="select"
          :items="['CPF', 'CNPJ']"
          :label="select"
          hide-details="true"
          outlined
        ></v-select>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="10">
        <items-data-table
          :items="items"
          :service="service"
          :search-text="searchText"
          @refecthItems="populateDataTable"
        ></items-data-table>
      </v-col>
    </v-row>
  </section>
</template>

<script>
import { validateCPF } from '@/utils/cpfValidator.js'
import { validateCNPJ } from '@/utils/cnpjValidator.js'

import CPFService from '@/services/CPFService.js'
import CNPJService from '@/services/CNPJService.js'

import ItemsDataTable from '@/components/ItemsDataTable.vue'

export default {
  name: 'Home',
  components: {
    ItemsDataTable
  },
  watch: {
    select() {
      this.populateDataTable()
    }
  },
  computed: {
    rules() {
      return {
        validate: item => this.validator(item) || `${this.select} inválido`
      }
    },
    mask() {
      return this.select == 'CPF' ? '###.###.###-##' : '##.###.###/####-##'
    },
    service() {
      return this.select == 'CPF' ? CPFService : CNPJService
    },
    validator() {
      return this.select == 'CPF' ? validateCPF : validateCNPJ
    }
  },
  data() {
    return {
      addDialog: false,
      itemToBeAdded: '',

      select: 'CPF',
      searchText: '',

      items: []
    }
  },
  mounted() {
    this.populateDataTable()
  },
  methods: {
    populateDataTable() {
      this.service.all()
      .then((response) => {
        this.items = []
        response.data.results.forEach(element => {
          let baseElement = {
            id: element.id,
            created_at: element.created_at,
            blocked: element.blocked_at ? 'Sim' : 'Não',
          }

          let mutableElement = this.select == 'CPF'
          ? { cpf: element.cpf }
          : { cnpj: element.cnpj }

          this.items.push({
            ...baseElement,
            ...mutableElement
          })
        })
      })
    },

    async addItem() {
      if(this.validator(this.itemToBeAdded)) {
        await this.service.create(this.itemToBeAdded)

        this.closeAddDialog()
        this.populateDataTable()
      }
    },
    closeAddDialog() {
      this.itemToBeAdded = ''
      this.addDialog = false
    },

  }
}
</script>