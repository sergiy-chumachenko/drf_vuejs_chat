<template>
    <div>
        <h1>Vue.js Chat</h1>
        <button @click="goLogin">Enter</button>
    </div>
</template>

<script>
    export default {
        name: "Home",
        methods: {
            goLogin() {
                this.$router.push({name: "login"})
            }
        }
    }
</script>

<style scoped>

</style>
