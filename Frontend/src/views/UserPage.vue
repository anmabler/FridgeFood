<template>
  <form @submit.prevent="postIngredients" action="post">
      <label for="ingredient">Add ingredient</label>
      <input type="text" id="ingredient" v-model="ingredient">
      <button type="submit">Add</button>
  </form>
</template>

<script>
export default {
    data (){
        return {
            ingredient:null
        }
    },
    methods: {

        }
    }

}
</script>

<style scoped>
label {
    display: block;
}

</style>