module.exports = {
  devServer: {
    host: 'localhost',
    port: 8080,
    https: false,
    // 以上的ip和端口是我们本机的;下面为需要跨域的
    proxy: { // 配置跨域
      '/api': {
        target: 'http://localhost:5000', // 这里后台的地址模拟的;应该填写你们真实的后台接口
        ws: true,
        changOrigin: true // 允许跨域
      },
      '/get_data': {
        target: 'http://localhost:5000', // 这里后台的地址模拟的;应该填写你们真实的后台接口
        ws: true,
        changOrigin: true // 允许跨域
      }
    }
  }
}
// if (process.env.NODE_ENV == 'development') {
//
//     axios.defaults.baseURL = '/api';
//
// }else if (process.env.NODE_ENV == 'debug') {
//
//     axios.defaults.baseURL = 'http://v.juhe.cn';
//
// }else if (process.env.NODE_ENV == 'production') {
//
//     axios.defaults.baseURL = 'http://v.juhe.cn';
//
// }
