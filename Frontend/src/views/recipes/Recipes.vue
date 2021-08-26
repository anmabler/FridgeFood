<template>
  <div v-if="recipes.length">
      <h1>Recipes</h1>
      <div v-for="recipe in recipes" :key="recipe.id" class="recipe">
        <h2>{{ recipe.title }}</h2>
      </div>
  </div>
  <div v-else>
    Loading recipes...
  </div>
</template>

<script>
export default {
  data (){
    return{
      recipes: []
    }
  },
  mounted() {
    fetch('http://localhost:3000/api/recipes/findByIngredients')
    .then(res => res.json()) // parse
    .then(data => this.recipes = data) // populate recipes-prop with the data from the API
    .catch(err => console.log(err.message)) // if there is an error, log the error message in the console
  }

}
</script>

<style scoped>
.class{
  background-color: blanchedalmond;
}

</style>