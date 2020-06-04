import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    data: []
  },
  mutations: {
    set_data (state, value) {
      state.data = value
    }
  },
  actions: {
  },
  modules: {
  }
})
