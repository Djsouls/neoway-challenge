<template>
  <v-app dark>
    <the-app-bar></the-app-bar>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import TheAppBar from './components/TheAppBar.vue'
export default {
  name: 'App',

  data: () => ({
    //
  }),

  components: {
    TheAppBar,
  }
};
</script>
