import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'
import Recipes from './views/recipes/Recipes.vue'
import RecipeDetails from './views/recipes/RecipeDetails.vue'
import ErrorPage from './views/ErrorPage.vue'
import SearchPage from './views/SearchPage.vue'
import UserPage from './views/UserPage.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/recipes',
        name: 'Recipes',
        component: Recipes
    },
    {
        path: '/recipes/:id', // route parameter
        name: 'RecipeDetails',
        component: RecipeDetails,
        props: true
    },
    {
        path: '/search',
        name: SearchPage,
        component: SearchPage
    },
    {
        path: '/users/:id',
        name: UserPage,
        component: UserPage,
        props: true
    },
    
    {
        path: '/:catchAll(.*)',
        name: 'ErrorPage',
        component: ErrorPage
    }
]
const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router