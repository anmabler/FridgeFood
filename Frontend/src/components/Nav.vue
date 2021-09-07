<template>
  <div>
        <h1>FRIDGEFOOD</h1>
        <ul>
            <li><router-link to="/search">Search</router-link></li>
            <li><router-link to="/users/1">Userpage</router-link></li>
        </ul> 
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
ul {
    display: inline-block;
    list-style-type: none;
    margin: 0;
    padding: 0;
}
div {
    /* margin-top: 20px; */
    background-color: bisque;
}

</style>