/* eslint-disable */
import Vue from 'vue';
import Router from 'vue-router';
const routerOptions = [
  {
    path: '/',
    component: 'Top'
  },
  {
    path: '/feeds',
    component: 'Feeds'
  },
  {
    path: '/ping',
    component: 'Ping'
  },
  {
    path: '/add',
    component: 'Add'
  },
  {
    path: '/top',
    component: 'Top'
  },
  { path: '*', component: 'NotFound' }
]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})
Vue.use(Router)
export default new Router({
  routes,
  mode: 'history'
})
