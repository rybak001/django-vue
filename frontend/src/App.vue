<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Home</strong></router-link>
        <router-link to="/" class="navbar-item"><strong>Add Post</strong></router-link>
      </div>
      <div class="navbar-start">
        <div class="navbar-item">
          <form method="get" action="/search">
            <div class="field has-addons">
              <div class="control is-expanded">
                <input type="text" class="input" placeholder="What are you looking for?" name="query">
              </div>
              <div class="control">
                <button class="button is-success">
                  <span class="icon">
                    <i class="fas fa-search"></i>
                  </span>
                </button>
              </div>
            </div>
          </form>
        </div>
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

    <footer class="footer">
    </footer>
  </div>
</template>

<style lang="scss">
@import '../node_modules/bulma';
</style>
