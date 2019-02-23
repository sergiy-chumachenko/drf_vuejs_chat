<template>
    <div>
        <h1>Vue.js Chat</h1>
        <button v-if="!auth" @click="goLogin">Enter</button>
        <button v-else @click="logout">Logout</button>
        <room v-if="auth"></room>
    </div>
</template>

<script>
    import Room from '@/components/Room'

    export default {
        name: "Home",
        components: {
            Room
        },
        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true;
                }
            }
        },
        methods: {
            goLogin() {
                this.$router.push({name: "login"});
            },
            logout() {
                sessionStorage.removeItem("auth_token");
                window.location = '/';
            }
        }
    }
</script>

<style scoped>

</style>
