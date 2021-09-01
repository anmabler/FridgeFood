<template>
  <form @submit.prevent="saveSearchToList">
      <label for="searchField">Search </label>
      <input v-model="searchInput" type="text" id="searchField" required>
      <small id="searchHelp">To search for multiple ingredients, add a comma (,) between each ingredient.</small>
      <button type="submit" >Search</button>
  </form>
  <div v-if="searchInputList.length">
    <h3>Your search:</h3>
    <div v-for="word in this.$store.getters.trimmedInput" :key="word"> {{word}}</div>
  </div>
</template>

<script>
export default {
  
  data() {
    return {
      searchInput : '',
      searchInputList: [],
      trimmedInput: [],
      queryString: ''
    }
  },
  
  methods: {
    search(){
      this.saveSearchToList()
      console.log("You pressed the search button");
      
    },
    saveSearchToList(){
       this.searchInputList = this.searchInput.split(',') // Split the input at ',' since I want the user to be able to input multiple ingredients.
      for (let word of this.searchInputList){
        this.trimmedInput.push(word.trim())  // Trim spaces before and after the word.   
        // console.log(word);
      }
      this.queryString = this.trimmedInput.join(',+') // Join the trimmed words to a string with ,+ which is needed for the endpoint.
      // console.log(this.queryString);

      this.$store.commit('setQueryString', this.queryString)
      this.$store.commit('setSearchInput', this.searchInput)
      this.$store.commit('setTrimmedInput', this.trimmedInput)
      console.log(this.$store.state.queryString);

      // this.$router.push('/recipes')
    }
  }


}
</script>

<style scoped>

label, small {
  display: block
}

</style>