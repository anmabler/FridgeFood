import { createStore } from 'vuex'

const state = {
    recipes : [],
    recipe : null,
    searchInput : '',
    searchInputList: [],
    queryString : '',

}

const getters = {
    recipes: state => {
        return state.recipes
    },
    recipe: state => {
        return state.recipe
    },
    searchInput: state => {
        return state.searchInput
    },
    searchInputList: state => {
        return state.searchInputList
    }

}

const mutations = {
    getRecipes(state, recipeList){
        state.recipes = recipeList
    },
    getRecipeDetails(state, recipe){
        state.recipe = recipe
    },
    setSearchInput(state, searchInput){
        state.searchInput = searchInput
    },
    setQueryString(state, queryString){
        state.queryString = queryString
    },
    
    setSearchInputList(state, searchInputList){
        state.searchInputList = searchInputList
    }
}

const actions = {
    async getRecipes(store) {
        let recipes = await fetch('http://localhost:3000/api/recipes/findByIngredients/' + state.queryString)
        recipes = await recipes.json() 
        store.commit('getRecipes', recipes)
    },
    async getRecipeById(store, id) {
        let recipe = await fetch('http://localhost:3000/api/recipes/findById/' + id)
        recipe = await recipe.json()
        store.commit('getRecipeDetails', recipe)

    },
}

export default createStore({state, getters, mutations, actions})