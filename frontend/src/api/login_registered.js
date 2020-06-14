function login (form) {
  const axios = require('axios')
  // 注意设置代理
  var res = axios.post(
    '/api/login', form, {
      headers: {
        'Content-Type': 'application/json'
      }
    }).then(
    function (res) {
      return res.data
    }
  ).catch(
    function (err) {
      console.log('error during login!')
      return err
    }
  )
  console.log(res.then())
}

export {
  login
}
