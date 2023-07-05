<template>
    <div class="add-post">
      <h1>Add Post</h1>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="title">Title:</label>
          <input type="text" id="title" v-model="title" required>
        </div>
        <div class="form-group">
          <label for="author">Author:</label>
          <select id="author" v-model="author" required>
            <option v-for="user in users" :value="user.username" :key="user.id">{{ user.username }}</option>
          </select>
        </div>
        <div class="form-group">
          <label for="body">Body:</label>
          <textarea id="body" v-model="body" required></textarea>
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
</template>
  
<script>
import axios from 'axios';
  
    export default {
        name: 'AddPost',
        data() {
        return {
            title: '',
            author: '',
            body: '',
            users: [], // Array to store the list of users from the backend
        };
        },
        mounted() {
        this.fetchUsers(); // Fetch the list of users when the component is mounted
        },
        methods: {
        fetchUsers() {
            axios
                .get('/api/v1/userview/') // Replace with your backend API endpoint to fetch users
                .then(response => {
                this.users = response.data;
            })
            .catch(error => {
                console.error(error);
            });
        },
        submitForm() {
            const postData = {
            title: this.title,
            author: this.author,
            body: this.body,
            };
            
            const token = localStorage.getItem('token'); // Retrieve the authentication token from local storage

            axios.post('/api/v1/posts/add-post/', postData, {
              headers: {
                Authorization: `Token ${token}`, // Include the token in the request headers
              },
            }) 
            .then(response => {
                console.log(response.data);
                // Handle success, e.g., show a success message or navigate to another page
                this.$router.push('/'); // Redirect to the home page
            })
            .catch(error => {
                console.log(error);
                // Handle error, e.g., show an error message to the user
            });
        },
    },
  };
</script>
  
<style>
  .add-post {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .add-post label {
    display: block;
    margin-bottom: 10px;
  }
  
  .add-post input,
  .add-post textarea {
    width: 100%;
    padding: 5px;
    margin-bottom: 10px;
  }
  
  .add-post button {
    background-color: #3273dc;
    color: #fff;
    padding: 8px 16px;
    border: none;
    cursor: pointer;
  }
</style>
  