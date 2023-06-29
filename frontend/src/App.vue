<template>
  <div id="wrapper">
      <nav class="navbar is-dark">
        <div class="navbar-brand">
          <router-link to="/" class="navbar-item"><strong>Home</strong></router-link>
          <router-link to="/" class="navbar-item"><strong>Add Post</strong></router-link>
        </div>

        <div class="navbar-menu" id="navbar-menu">
          <div class="navbar-end">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light">Login</router-link>
            </div>
          </div>
        </div>
      </nav>

      <section class="section">
        <router-view/>
      </section>

      <footer class ="footer">
      </footer>
  </div>
</template>

<style lang="scss">
@import '../node_modules/bulma';
</style>
