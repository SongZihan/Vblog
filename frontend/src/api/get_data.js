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
function get_one_page (self, article_id) {
  self.$axios({
    method: 'get',
    url: '/get_data/get_one_page',
    params: { id: article_id }
  }).then(function (res) {
    self.$router.push({
      name: 'article',
      params: { data: res.data }
    })
  })
}

export {
  firstGetData, get_one_page
}
