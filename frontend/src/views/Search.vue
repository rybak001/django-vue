<template>
    <div class="page-search">
      <div class="columns is-multiline">
        <div class="column is-12">
          <h1 class="title">Search</h1>
          <h2 class="is-size-5 has-text-grey">Search term: "{{ query }}"</h2>
        </div>
        <div class="column is-12">
          <div class="columns is-multiline">
            <div class="column is-12" v-for="post in posts" :key="post.pk">
              <Postbox :post="post" />
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios'
import Postbox from '@/components/Postbox'
export default {
    name: 'Search',
    components: {
        Postbox
    },
    data() {
        return {
            posts: [],
            query: ''
        }
    },
    mounted() {
        document.title = 'Search | Blog'

        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')) {
            this.query = params.get('query')

            this.performSearch()
        }
    },
    methods: {
        performSearch() {
            axios
                .post('/api/v1/posts/search/', {'query': this.query})
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
