import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '../pages/Index'
import Login from '../pages/Login'
import Registered from '../pages/Registered'
import store from '../store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Index',
    component: Index
  },
  {
    path: '/Login',
    name: 'Login',
    component: Login
  },
  {
    path: '/Registered',
    name: 'Registered',
    component: Registered
  }
]
// 解决路由重复push报错 https://blog.csdn.net/xiecheng1995/article/details/106497172/
const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push (location) {
  return originalPush.call(this, location).catch(err => err)
}
// 页面刷新时，重新赋值token
if (sessionStorage.getItem('token')) {
  store.commit('set_token', sessionStorage.getItem('token'))
}

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
