<template>
  <section class="py-8">
    <v-btn fab fixed bottom right color="primary">
      <v-icon>mdi-plus</v-icon>
    </v-btn>

    <v-row justify="center">
      <v-col cols="10">
        <v-data-table :items="values" :headers="headers"></v-data-table>
      </v-col>
    </v-row>
  </section>
</template>

<script>

export default {
  name: 'Home',
  computed: {
    headers() {
      return [
        { text: 'id', value: 'id'},
        { text: 'cpf', value: 'cpf'},
        { text: 'created_at', value: 'created_at'},
      ]  
    }
  },
  data() {
    return {
      values: [
        { id: 0, cpf: '81729831131', created_at: new Date() },
        { id: 1, cpf: '81729831131', created_at: new Date() },
        { id: 2, cpf: '81729831131', created_at: new Date() },
        { id: 3, cpf: '81729831131', created_at: new Date() },
        { id: 4, cpf: '81729831131', created_at: new Date() },
        { id: 5, cpf: '81729831131', created_at: new Date() },
        { id: 6, cpf: '81729831131', created_at: new Date() },
        { id: 7, cpf: '81729831131', created_at: new Date() },
        { id: 8, cpf: '81729831131', created_at: new Date() },
        { id: 9, cpf: '81729831131', created_at: new Date() },
        { id: 10, cpf: '81729831131', created_at: new Date() },
        { id: 11, cpf: '81729831131', created_at: new Date() },
        { id: 12, cpf: '81729831131', created_at: new Date() },
      ]
    }
  }
}
</script>
