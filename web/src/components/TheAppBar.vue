<template>
  <v-app-bar color="primary">
    <v-app-bar-nav-icon v-if="!isHome">
      <router-link to="/">
        <v-icon color="white">mdi-chevron-left</v-icon>
      </router-link>
    </v-app-bar-nav-icon>
    <v-app-bar-nav-icon v-else>
      <router-link to="/validate">
        <v-icon color="black">mdi-chevron-left</v-icon>
      </router-link>
    </v-app-bar-nav-icon>
    <v-toolbar-title> Validação Fera! </v-toolbar-title>
  </v-app-bar>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  computed: {
    isHome() {
      return this.$route.name === 'Home'
    }
  },
})
</script>