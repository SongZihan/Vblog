function firstGetData (self) {
  // const axios = require('axios')
  // 注意设置代理
  self.$axios.get('/get_data/homepage').then(
    function (res) {
      // 将文章数据存入vuex
      self.$store.commit('set_data', res.data.data)
    }
  ).catch(
    function (err) {
      console.log(err)
    }
  )
}

export {
  firstGetData
}
