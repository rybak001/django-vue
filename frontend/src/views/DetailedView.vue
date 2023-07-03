<template>
    <div class="page-product">
      <div class="columns is-multiline">
        <div class="column is-9">
          <h1 class="title">{{ post.title }}</h1>
          <h1 class="subtitle is-5">By: {{ post.author }}</h1>
          <p class="paragraph is-1">{{ post.body }}</p>
        </div>
      </div>
    </div>
</template>
  
<script>
import axios from 'axios'
  
    export default {
    name: "DetailedView",
    data() {
      return {
        post: {},
      }
    },
    mounted() {
      this.getPost()
    },
    methods: {
      getPost() {
        const pk = this.$route.params.pk
  
        axios
          .get(`/api/v1/posts/${pk}`)
          .then(response => {
            this.post = response.data
          })
          .catch(error => {
            console.log(error)
          })
      }
    }
  }
  </script>
  