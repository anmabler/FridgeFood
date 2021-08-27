import { createStore } from 'vuex'

const state = {
    recipes : [],
    recipe : null
}

const getters = {
    RECIPES : state => {
        return state.recipes
    },
    RECIPE : state => {
        return state.recipe
    }

}

const mutations = {
    setRecipes(state, recipeList){
        state.recipes = recipeList
    },
    getRecipeDetails(state, recipe){
        state.recipe = recipe
    }
}

const actions = {
    async getRecipes(store) {
        let recipes = await fetch('http://localhost:3000/api/recipes/findByIngredients')
        recipes = await recipes.json() 
        store.commit('setRecipes', recipes)
    },
    async getRecipeById(store, id) {
        let recipe = await fetch('http://localhost:3000/api/recipes/findById/' + id)
        recipe = await recipe.json()
        store.commit('getRecipeDetails', recipe)

        // .catch(err => console.log(err.message))
    }
}

export default createStore({state, getters, mutations, actions})