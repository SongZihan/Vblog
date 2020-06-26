<template>
  <div>
    <el-row v-for="(i,index) in my_data" :key="index">
      <el-col>
        <div>
          <el-card class="box-card" shadow="hover">
            <div slot="header" class="clearfix" @click="to_write(i)">
              <span><h2>{{i[1]}}</h2></span>
            </div>
            <el-button type="danger" style="float: right" icon="el-icon-delete" @click="del_draft(i[0])"
                       circle></el-button>
          </el-card>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { get_draft } from '../api/get_data'

export default {
  name: 'Draft_display',
  computed: {
    // 计算属性实时返回state中的变化
    my_data () {
      return this.$store.state.draft_data
    }
  },
  methods: {
    to_write (i) {
      this.$router.push({
        name: 'Write',
        params: { data: i }
      })
    },
    del_draft (id) {
      this.$axios({
        method: 'post',
        url: '/api/manage_draft',
        data: {
          id: id,
          type: 'del'
        }
      }).then(
        (res) => {
          if (res.data.code === 200) {
            // 删除成功刷新数据
            get_draft(this)
          }
        }
      )
    }
  }
}
</script>

<style scoped>

</style>
