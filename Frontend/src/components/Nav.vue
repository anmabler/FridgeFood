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
    list-style-type: none;
    margin: 0;
    padding: 0;
}
li {
    display: inline;
}
a {
    padding: 10px
}
div {
    /* margin-top: 20px; */
    background-color: bisque;
    padding-bottom: 10px;
}

</style>