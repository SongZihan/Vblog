<template>

  <div>
    <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
      <el-form-item label="ID" prop="ID">
        <el-input  v-model="ruleForm.ID" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="密码" type="password" prop="pass">
        <el-input v-model.number="ruleForm.pass"></el-input>
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
// import to_registered from '../lib/helper'
export default {
  name: 'Login',
  data () {
    // 添加了一些辅助验证，可以在提交前对表单格式进行验证
    var checkID = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('ID不能为空'))
      }
      setTimeout(() => {
        if (value.length < 5 || value.length > 20) {
          callback(new Error('请输入正确的ID'))
        }
      }, 1000)
    }
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      }
    }

    return {
      ruleForm: {
        ID: '',
        pass: ''
      },
      rules: {
        pass: [
          { validator: validatePass, trigger: 'blur' }
        ],
        ID: [
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
    }
  }
}
</script>

<style scoped>

</style>
