<template>
    <div v-if="recipe">
        <h1>{{ recipe.title }}</h1>
        <p>Servings: {{ recipe.servings }}</p>
        <p>Ready in: {{ recipe.readyInMinutes }} minutes</p>
        <img :src="recipe.image" :alt="recipe.title">
        <ul>
            <li class="ingredients" v-for="ingredient in recipe.extendedIngredients" :key="ingredient.name"> {{ ingredient.name }} {{ingredient.amount}} {{ ingredient.unit}} </li>
        </ul>

        <!-- If the recipe does not have instructions, show a link to the source url. -->
        <div v-if="recipe.length">
            <p>Instructions: {{ recipe.instructions}}</p>
        </div>
        <div v-else>
            For instructions go to : <a v-bind:href="recipe.sourceUrl">{{ recipe.sourceName }}</a> 
        </div>
    </div>
    <div v-else>
        Loading recipe details...
    </div>
</template>

<script>
export default {
    computed: {
        recipe(){
            return this.$store.getters.RECIPE
        }
    },

    mounted() {
        this.$store.dispatch('getRecipeById', this.$route.params.id)
    }

}
</script>

<style scoped>
/* I'm choosing to capitalize the first letter of the ingredient-string with CSS since I only want it displayed as such. */ 
.ingredients::first-letter{
    text-transform: capitalize;
}

</style>