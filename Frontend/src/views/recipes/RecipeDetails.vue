<template>
    <div v-if="recipe">
        <h1>{{ recipe.title }}</h1>
        <p>Servings: {{ recipe.servings }}</p>
        <p>Ready in: {{ recipe.readyInMinutes }} minutes</p>
        <img :src="recipe.image" :alt="recipe.title">
        <ul>
            <li class="ingredients" v-for="ingredient in recipe.extendedIngredients" :key="ingredient.name"> {{ ingredient.name }} {{ingredient.amount}} {{ ingredient.unit}} </li>
        </ul>

        <!-- If the recipe does not have a description, go to the source url. -->
        <div v-if="recipe.length">
            <p>Instructions: {{ recipe.instructions}}</p>
        </div>
        <div v-else>
            For instructions go to : <a v-bind:href="recipe.sourceUrl">{{ recipe.sourceName }}</a> 
        </div>
    </div>
    <div v-else>
        Loading...
    </div>
</template>

<script>
export default {
    props: ['id'],
    data (){
        return {
            recipe: null,
        }
    },
    methods: {
        
        
    },
    mounted() {
        fetch('http://localhost:3000/api/recipes/findById/' + this.id)
        .then(res => res.json()) // parse
        .then(data => this.recipe = data) // populate recipes-prop with the data from the API
        .catch(err => console.log(err.message))
    }
    // data() {
    //     return {
    //         name: this.$route.params.name
    //     }
    // }

}
</script>

<style scoped>
.ingredients::first-letter{
    text-transform: capitalize;
}

</style>