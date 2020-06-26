import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    data: [],
    is_login: false,
    token: '',
    draft_data: ''
  },
  mutations: {
    set_data (state, value) {
      // 整理数据格式 [['分类名',obj,obj],['分类名',obj]...]
      var _ = require('lodash')
      const classify = _.uniqBy(value, value => value[2])
      // console.log('classify is', classify)
      var result = []
      for (var i in classify) {
        // 创建一个大分类
        var item = []
        item.push(classify[i][2])
        for (var j in value) {
          if (classify[i][2] === value[j][2]) {
            item.push(value[j])
          }
        }
        result.push(item)
      }
      // console.log(result)
      state.data = result
    },
    set_draft_data (state, data) {
      state.draft_data = data
    },

    set_token (state, token) {
      // 顺便修改登录状态
      state.is_login = true
      state.token = token
      sessionStorage.token = token
    },
    del_token (state) {
      // 顺便修改登录状态
      state.is_login = false
      state.token = ''
      sessionStorage.removeItem('token')
    }
  },
  actions: {
  },
  modules: {
  }

})
