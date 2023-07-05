<template>
    <div class="page-log-out">
      <div class="columns">
        <div class="column is-4 is-offset-4">
          <h1 class="title">Log out</h1>
  
          <button class="button is-dark" @click="logout">Log out</button>
  
          <hr>
        </div>
      </div>
    </div>
</template>
  
<script>
  import axios from 'axios'
  
  export default {
    name: 'Logout',
    mounted() {
      document.title = 'Log Out'
    },
    methods: {
      logout() {
        const token = localStorage.getItem('token') // Retrieve the authentication token from local storage
  
        axios.post('/api/v1/token/logout', {}, {
          headers: {
            Authorization: `Token ${token}`, // Include the token in the request headers
          },
        })
        .then(response => {
          console.log(response)
          this.$store.commit('setToken', '') // Clear the token from the store
          delete axios.defaults.headers.common['Authorization'] // Remove the token from the request headers
          localStorage.removeItem('token') // Remove the token from local storage
          this.$router.push('/')
        })
        .catch(error => {
          console.log(error)
        })
      },
    },
  }
</script>
  