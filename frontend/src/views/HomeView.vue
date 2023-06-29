<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <div class="container">
          <p class="title mb-6">
            <span class="icon is-large">
              <i class="fas fa-pencil-alt"></i>
            </span>
            Welcome to Ryan's Blog
          </p>
          <p class="subtitle">
            The best online blog platform to exist
          </p>
        </div>
      </div>
    </section>

    <div class="container">
      <div class="columns is-multiline">
        <div class="column is-12">
          <h2 class="title is-2 has-text-centered">Blog Posts:</h2>
        </div>
        <div class="column is-12" v-for="post in posts" :key="post.pk">
          <div class="box">
            <div class="action-icons">
              <div class="edit-icon">
                <i class="fas fa-pencil-alt"></i>
              </div>
              <div class="delete-icon">
                <i class="fas fa-times"></i>
              </div>
            </div>
            <h3 class="title is-2">{{ post.title }}</h3>
            <h1 class="subtitle is-5">By: {{ post.author }}</h1>
            <p class="paragraph is-1">{{ post.body }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HomeView',
  data() {
    return {
      posts: []
    }
  },
  mounted() {
    this.PostViewList()
  },
  methods: {
    PostViewList() {
      axios
        .get('/api/v1/posts')
        .then(response => {
          this.posts = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>
.home {
  padding: 20px;
}

.hero.is-medium {
  padding: 2rem;
}

.box {
  padding: 20px;
  border-radius: 5px;
  background-color: #f5f5f5;
  position: relative;
}

.title.is-2 {
  margin-top: 10px;
}

.subtitle.is-5 {
  margin-top: 10px;
  color: #888;
}

.container {
  width: 100%;
  max-width: 960px;
  margin: 0 auto;
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
