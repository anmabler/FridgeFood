<template>
  <form @submit.prevent="search">
      <label>Search </label>
      <input v-model="searchInput" type="text"/>
      <button type="submit" >Search</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      searchInput : ''
    }
  },
  methods: {
    search(){
      console.log("You pressed the search button");
    }
  },


}
</script>

<style>

</style>