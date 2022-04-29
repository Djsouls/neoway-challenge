<template>
  <v-app-bar color="primary" max-height="100">
    <v-app-bar-nav-icon v-if="!isHome">
      <router-link to="/">
        <v-icon color="white">mdi-chevron-left</v-icon>
      </router-link>
    </v-app-bar-nav-icon>
    <v-toolbar-title v-if="!isHome">Home</v-toolbar-title>
    <v-toolbar-title v-if="isHome">
      Validações
    </v-toolbar-title>
    <v-app-bar-nav-icon v-if="isHome">
      <router-link to="/validate">
        <v-icon color="white">mdi-chevron-right</v-icon>
      </router-link>
    </v-app-bar-nav-icon>
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