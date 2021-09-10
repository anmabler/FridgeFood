<template>
  <div>
    <div v-if="recipes.length">
        <h1>Recipes</h1>
        <div v-for="recipe in recipes" :key="recipe.id" class="recipe" >
          <router-link :to="{ name : 'RecipeDetails', params : { id : recipe.id }}">
            <h2>{{ recipe.title }}</h2>
            <img :src="recipe.image" :alt="recipe.title">
          </router-link>
        </div>
    </div>
    <div v-else>
      Loading recipes...
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    recipes(){
      return this.$store.getters.recipes
    }
  },
 
  beforeCreate (){


  },

  mounted() {
    this.$store.dispatch('getRecipes')
  }

}
</script>

<style scoped>
.recipe{
  background-color: blanchedalmond;
  margin-bottom: 50px;
  padding-top: 10px;
  padding-bottom: 20px;
}

</style>