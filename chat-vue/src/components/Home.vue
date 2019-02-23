<template>
    <mu-container>
        <mu-appbar style="width: 100%;" color="primary">
            Vue.js Chat
            <mu-button flat slot="right" v-if="!auth" @click="goLogin">LOGIN</mu-button>
            <mu-button flat slot="right" v-else @click="logout">LOGOUT</mu-button>
        </mu-appbar>
        <mu-row><h1></h1></mu-row>
        <mu-row>
            <Room v-if="auth" @openDialog="openDialog"></Room>
            <Dialog v-if="dialog.show" :id="dialog.id"></Dialog>
        </mu-row>
    </mu-container>
</template>

<script>
    import Room from '@/components/rooms/Room.vue'
    import Dialog from '@/components/rooms/Dialog.vue'

    export default {
        name: "Home",
        components: {
            Room,
            Dialog
        },
        data() {
            return {
                dialog: {
                    id: '',
                    show: false
                }
            }
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
            },
            openDialog(id) {
                this.dialog.id = id;
                this.dialog.show = true;
            }
        }
    }
</script>

<style scoped>

</style>
