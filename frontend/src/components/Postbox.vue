<template>
    <div class="box post-box">
      <div class="post-content">
        <div class="action-icons">
          <div class="edit-icon" @click="editPost(post.pk)">
            <i class="fas fa-pencil-alt"></i>
          </div>
          <div class="delete-icon" @click="deletePost(post.pk)">
            <i class="fas fa-times"></i>
          </div>
        </div>
        <h3 class="title is-2">{{ post.title }}</h3>
        <h1 class="subtitle is-5">By: {{ post.author }}</h1>
        <router-link :to="`/api/v1/posts/${post.pk}`" class="view-details-link">
          View Details
        </router-link>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Postbox',
    props: {
      post: Object,
    },
    methods: {
      editPost(pk) {
        // Handle the edit functionality
      },
      deletePost(pk) {
        axios
          .delete(`/api/v1/posts/delete/${pk}`)
          .then((response) => {
            console.log(response.data.message);
            this.$emit('post-deleted', pk);
            // Handle the successful deletion
          })
          .catch((error) => {
            console.log(error);
            // Handle the error
          });
      },
    },
  };
  </script>
  
<style scoped>
  .box.post-box {
    padding: 20px;
    border-radius: 5px;
    background-color: #f5f5f5;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .post-content {
    position: relative;
  }
  
  .action-icons {
    position: absolute;
    top: 10px;
    right: 10px;
    display: flex;
  }
  
  .edit-icon,
  .delete-icon {
    cursor: pointer;
    transition: color 0.3s;
    margin-right: 10px;
  }
  
  .edit-icon {
    color: #3273dc; /* Blue color */
  }
  
  .delete-icon {
    color: #ff3860; /* Bright red color */
  }
  
  .edit-icon:hover,
  .delete-icon:hover {
    color: #ff0000; /* Red color when hovered */
  }
  </style>
  