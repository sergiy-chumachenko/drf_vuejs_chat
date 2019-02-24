<template>
    <div>
        <mu-container v-if="user_list.length > 0">
            <select v-model="option" >
                <option :value="user.id" v-for="user in user_list">
                    {{user.attributes.username}}
                </option>
            </select>
            <mu-button class="btn-send" round color="success" @click="addUser">Add User</mu-button>
        </mu-container>
        <mu-container v-else>
            <p><strong>All users has already added to the Room!</strong></p>
        </mu-container>
    </div>
</template>

<script>
    export default {
        name: "AddUsers",
        props: {
            room: ''
        },
        data() {
            return {
                option: '',
                user_list: ''
            }
        },
        created() {
            this.loadUsers()
        },
        methods: {
            loadUsers() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/chat/users/',
                    type: "GET",
                    data: {
                        room: parseInt(this.room),
                    },
                    success: (response) => {
                        this.user_list = response.data;
                    }
                })
            },
            addUser() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/chat/users/',
                    type: "POST",
                    data: {
                        room: this.room,
                        user: parseInt(this.option)
                    },
                    success: (response) => {
                        alert("User has added!");
                        this.loadUsers();
                    },
                    error: (response) => {
                        alert("Error! User has not added!")
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>
