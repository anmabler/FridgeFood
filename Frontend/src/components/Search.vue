<template>
  <div>
    <form @submit.prevent="saveSearchToList">
        <label for="searchField">Search </label>
        <input v-model="searchInput" type="text" id="searchField" required>
        <small id="searchHelp">To search for multiple ingredients, add a comma (,) between each ingredient.</small>
        <button type="submit" >Search</button>
    </form>
    <div v-if="searchInput.length">
      <h3>Your search:</h3>
      <p>{{searchInput}}</p>
    </div>
  </div>
</template>

<script>
export default {
  computed : {
    searchInput: {
      get (){
        return this.$store.getters.searchInput
      },
      set (value) {
        this.$store.commit('setSearchInput', value)
      }
    },
    searchInputList: {
      get(){
        return this.$store.getters.searchInputList
      },
      set(value){
        this.$store.commit('setSearchInputList', value)
      }
    },
    queryString: {
      get(){
        return this.$store.getters.queryString
      },
      set(value){
        this.$store.commit('setQueryString', value)
      }

    }
    
  },
  
  data() {
    return {
      trimmedInput: [],
    }
  },
  
  methods: {
    search(){
      console.log("You pressed the search button");
      
    },
    saveSearchToList(){
      this.searchInputList = []
      this.trimmedInput = []
      this.searchInputList = this.searchInput.split(',') // Split the input at ',' since I want the user to be able to input multiple ingredients.
      for (let word of this.searchInputList){
        this.trimmedInput.push(word.trim())  // Trim spaces before and after the word.   
      }
      this.queryString = this.trimmedInput.join(',+')
      this.$router.push('/recipes')
    }
    
  }


}
</script>

<style scoped>

label, small {
  display: block
}


</style>