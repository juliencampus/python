import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Index',
    component: () => import('@/views/Index.vue')
  },
  {
    path:'/new',
    name: 'New',
    component: () => import('@/views/NewA.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
