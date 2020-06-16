<template>

  <div>
    <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
      <el-form-item label="ID" prop="username">
        <el-input  v-model="ruleForm.username" autocomplete="on"></el-input>
      </el-form-item>
      <el-form-item label="密码" type="password" prop="password">
        <el-input v-model.number="ruleForm.password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
        <el-button @click="resetForm('ruleForm')">重置</el-button>
        <el-button @click="to_registered">注册</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>

export default {
  name: 'Login',
  data () {
    // 添加了一些辅助验证，可以在提交前对表单格式进行验证
    var checkID = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('ID不能为空'))
      } else {
        callback()
      }
    }
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        callback()
      }
    }

    return {
      ruleForm: {
        username: '',
        password: ''
      },
      rules: {
        password: [
          { validator: validatePass, trigger: 'blur' }
        ],
        username: [
          { validator: checkID, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    to_registered: function () {
      this.$router.push('Registered')
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // 转换为字符串
          this.ruleForm.password += ''
          this.ruleForm.username += ''
          // 发起post请求
          this.$axios({
            method: 'post',
            url: '/api/login',
            data: this.ruleForm
          }).then((res) => {
            if (res.data.code === 200) {
              // 设置token到全局存储
              const token = res.data.data
              this.$store.commit('set_token', token)
              // 实时更新token到全局请求头中 header['Authorization']
              this.$axios.defaults.headers.common.Authorization = token
              // 输出成功信息
              this.$notify({
                title: '登录成功',
                message: token,
                type: 'success'
              })
              // 登录完成返回主页
              this.$router.push('/')
              // 登录完成设置登出
            } else {
              console.log(res.data.data)
            }
          }).catch(
            function (err) {
              console.log(err)
            }
          )
        } else {
          console.log('error submit!!')
          return false
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
