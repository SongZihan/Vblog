function firstGetData () {
  const axios = require('axios')
  // 注意设置代理
  return axios.get('/api/first_get').then(
    function (res) {
      return res.data
    }
  ).catch(
    function (err) {
      console.log('error during get data!')
      return err
    }
  )
}

export {
  firstGetData
}
