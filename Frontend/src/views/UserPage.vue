<template>
  <form @submit.prevent="postIngredients" action="post">
      <label for="ingredient">Add ingredient</label>
      <input type="text" id="ingredient" v-model="ingredient">
      <button type="submit">Add</button>
  </form>
  <div v-if="this.ingredient.length">{{ ingredient }}</div>
</template>

<script>
export default {
    data (){
        return {
            ingredient:'',

        }
    },
    methods: {
         async postIngredients(){
            try{
                let request = {
                    method: "POST",
                    url: "http://localhost:3000/users/1" ,
                    headers: { "Content-Type": "application/json"},
                    body: JSON.stringify({ 
                        name: this.ingredient })
     
                }
                await fetch("http://localhost:3000/api/users/1", request)
                
            } catch(error){
                console.log(error)
            }


        }

        }


        
    }


</script>

<style scoped>
label {
    display: block;
}

</style>