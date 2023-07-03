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
        <div class="column is-12">
          <Postbox v-for="post in posts" :key="post.pk" :post="post" 
          @post-deleted="handlePostDeleted"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Postbox from '@/components/Postbox'

export default {
  name: 'HomeView',
  data() {
    return {
      posts: []
    }
  },
  components: {
    Postbox
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
    },
    handlePostDeleted(pk) {
      // Remove the deleted post from the posts array
      this.posts = this.posts.filter((post) => post.pk !== pk);
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
</style>