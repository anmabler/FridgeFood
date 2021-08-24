<template>
    <div>
        <h1>Recipe details page</h1>
        <p>Recipe name is {{ name }}</p>
    </div>
</template>

<script>
export default {
    props: ['name']
    // data() {
    //     return {
    //         name: this.$route.params.name
    //     }
    // }

}
</script>

<style>

</style>