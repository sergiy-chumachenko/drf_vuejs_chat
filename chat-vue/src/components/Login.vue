<template>
    <div>
        <input v-model="login" type="text" placeholder="Login"/>
        <input v-model="password" type="password" placeholder="Password"/>
        <button @click="setLogin">Login</button>
    </div>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "Login",
        data() {
            return {
                login: '',
                password: '',
            }
        },
        methods: {
            setLogin() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/login",
                    type: "POST",
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        alert("Thank you!");
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token);
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Unable to login with provided credentials.")
                        }
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>
