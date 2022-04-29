<template>
  <v-dialog
    v-model="visibility"
    max-width="340"
    persistent
  >
    <v-card>
      <v-card-title class="text-h5">
        Tem certeza que gostaria de realizar essa operação?
      </v-card-title>
      <v-card-text>
        Essa ação irá alterar o estado deste item.
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="white"
          text
          @click="cancel"
        >
          Cancelar
        </v-btn>
        <v-btn
          color="white"
          text
          @click="confirm"
        >
          Confirmar
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>

export default {
  props: {
    visibility: {
      type: Boolean,
      default: false
    },
    callbackObject: {
      type: Object,
    }
  },
  methods: {
    cancel() {
      this.$emit('cancel')
    },
    async confirm() {
      let callback = this.callbackObject.callback
      let args = this.callbackObject.args

      await callback(...Object.values(args))
      .then((response) => {
        this.$emit('confirm', response)
      }).catch((response) => {
        this.$emit('error', response)
      });
    }
  }
}
</script>