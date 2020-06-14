import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import _ from 'lodash'
// element-ui
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
// markdown 编辑器 https://github.com/hinesboy/mavonEditor
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'

Vue.use(ElementUI)
Vue.use(mavonEditor)
Vue.config.productionTip = false

// 全局请求头
axios.defaults.headers.post['Content-Type'] = 'application/json;charset=UTF-8'
// 全局超时时间
axios.defaults.timeout = 10000

// 全局token
axios.defaults.headers.common.Authentication = store.state.token
Vue.prototype.$axios = axios
// lodash
Vue.prototype._ = _

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
