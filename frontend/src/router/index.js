import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DetailedView from '../views/DetailedView.vue'
import Search from '../views/Search.vue'
import LogIn from '../views/LogIn.vue'
import AddPost from '../views/AddPost.vue'
import LogOut from '../views/LogOut.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
  path: '/search',
  name: 'search',
  component: Search
  },
  {
  path: '/token/login',
  name: 'login',
  component: LogIn
  },
  {
  path: '/token/logout',
  name: 'logout',
  component: LogOut
  },
  {
    path: '/posts/add-post',
    name: 'addpost',
    component: AddPost
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/api/v1/posts/:pk',
    name: ' product',
    component: DetailedView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
