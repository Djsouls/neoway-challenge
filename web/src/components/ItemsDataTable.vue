<template>
  <v-data-table
    :items="items"
    :item-class="rowBackground"
    :headers="headers"
    :search="searchText"
  >
    <template v-slot:top>
      <confirm-dialog
        :visibility="showConfirmDialog"
        :callbackObject="confirmDialogCallbackObject"
        @cancel="closeConfirmDialog"
        @confirm="confirmOperation"
        @error="errorOperation"
      ></confirm-dialog>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-tooltip top>
        <template v-slot:activator="{ on }">
          <v-icon
            v-on="on"
            class="mr-2"
            small
            @click="blockItem(item)"
          >
            mdi-block-helper
          </v-icon>
        </template>
        <span>Bloquear esse item</span>
      </v-tooltip>
      <v-tooltip top>
        <template v-slot:activator="{ on }">
          <v-icon
            v-on="on"
            small
            @click="deleteItem(item)"
          >
            mdi-delete
          </v-icon>
        </template>
        <span>Deletar esse item</span>
      </v-tooltip>
    </template>
  </v-data-table>
</template>

<script>

import ConfirmDialog from '@/components/ConfirmDialog.vue'

export default {
  components: {
    ConfirmDialog
  },
  props: {
    items: {
      type: Array,
    },
    searchText: {
      type: String,
      default: '',
    },
    service: {
      type: Object,
    },
  },
  computed: {
    customHeader() {
      if(this.items.length) {
        const first = this.items[0]

        if('cnpj' in first) {
          return 'cnpj'
        }
      }

      return 'cpf'
    },
    headers() {  
      return [
        { text: 'id', value: 'id'},
        { text: this.customHeader, value: this.customHeader},
        { text: 'created_at', value: 'created_at'},
        { text: 'blocked', value: 'blocked'},
        { text: 'actions', value: 'actions', sortable: false},
      ]
    },
  },
  data() {
    return {
      showConfirmDialog: false,
      confirmDialogCallbackObject: {
        callback: undefined,
        args: undefined
      },
    }
  },
  methods: {
    blockItem(item) {
      this.service.block(item.id)
      this.confirmDialogCallbackObject.callback = this.service.block;
      this.confirmDialogCallbackObject.args = { id: item.id };

      this.showConfirmDialog = true;
    },
    deleteItem(item) {
      this.confirmDialogCallbackObject.callback = this.service.delete;
      this.confirmDialogCallbackObject.args = { id: item.id };

      this.showConfirmDialog = true;
    },
    closeConfirmDialog() {
      this.showConfirmDialog = false;
    },
    confirmOperation() {
      this.$emit('refecthItems')
      this.closeConfirmDialog()
    },
    errorOperation() {
      console.log('Deu ruim rapeize')
    },

    rowBackground(item) {
      return item.blocked == 'Sim' ? 'brown' : '';
    }
  }
}
</script>